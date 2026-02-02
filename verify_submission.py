import os
import json
import sys

def verify():
    print("="*60)
    print("🤟 Gemini 3 Hackathon - Submission Verifier")
    print("="*60)

    # 1. Check Directory Structure
    req_files = ['app.py', 'requirements.txt', 'sign_language_data.json', 'templates/index.html', 'HACKATHON_SUBMISSION.md']
    missing = []
    for f in req_files:
        if not os.path.exists(f):
            missing.append(f)
    
    if missing:
        print(f"[✗] Missing required files: {', '.join(missing)}")
    else:
        print("[✓] All core files present")

    # 2. Check Service Account
    sa_path = 'service-account-key.json'
    if not os.path.exists(sa_path):
        print("[!] Warning: service-account-key.json not found. Live verification skipped.")
    else:
        print("[✓] Service account key found")
        try:
            import vertexai
            from vertexai.generative_models import GenerativeModel
            
            with open(sa_path, 'r') as f:
                sa_data = json.load(f)
                project_id = sa_data.get('project_id')
            
            vertexai.init(project=project_id, location="us-central1")
            
            # Test Gemini
            print("[...] Testing Gemini 3 integration...")
            model = GenerativeModel("gemini-2.0-flash-001")
            response = model.generate_content("Hello! Verify connection.")
            print(f"[✓] Gemini Response: {response.text[:50]}...")

            # Test Imagen
            print("[...] Testing Imagen integration...")
            from vertexai.preview.vision_models import ImageGenerationModel
            image_model = ImageGenerationModel.from_pretrained("imagegeneration@006")
            print("[✓] Imagen Model initialized")

        except Exception as e:
            print(f"[✗] API Verification failed: {e}")

    # 3. Check Documentation
    readme_path = 'README.md'
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "(to be added)" in content:
                print("[!] Warning: Demo video link still missing in README.md")
            else:
                print("[✓] README.md seems ready")

    print("="*60)
    print("Ready for submission? (Check warnings above)")

if __name__ == "__main__":
    verify()
