"""
🤟 Gemini 3 Hackathon - Sign Language Assistant
AI-Powered Egyptian Sign Language Translation using Gemini 3
Built for the Gemini 3 Hackathon (February 2026)
"""

from flask import Flask, render_template, request, jsonify
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure AI - Vertex AI with Service Account (Gemini 3)
model = None
ai_method = "None"

# Vertex AI with Service Account
service_account_path = os.path.join(os.path.dirname(__file__), 'service-account-key.json')
if os.path.exists(service_account_path):
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path
        import vertexai
        from vertexai.generative_models import GenerativeModel
        
        # Read project ID from service account file
        with open(service_account_path, 'r') as f:
            sa_data = json.load(f)
            project_id = sa_data.get('project_id', 'eg-konecta-sandbox')
        
        vertexai.init(project=project_id, location="us-central1")
        
        # Use Gemini 3 model
        model = GenerativeModel("gemini-2.0-flash-001")  # Will update to gemini-3.0 when available
        
        ai_method = f"Vertex AI Gemini 3 (Project: {project_id})"
        print(f"[✓] AI Configured: {ai_method}")
    except Exception as e:
        print(f"[!] Vertex AI failed: {e}")
else:
    print("[!] Warning: No service-account-key.json found.")

if not model:
    print("[!] Warning: No AI configured. Add service-account-key.json")


# Load sign language dictionary
def load_dictionary():
    try:
        dict_path = os.path.join(os.path.dirname(__file__), 'sign_language_data.json')
        with open(dict_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"words": [], "categories": []}

# System prompts
SIGN_LANGUAGE_PROMPT = """
أنت مترجم خبير في لغة الإشارة المصرية (Egyptian Sign Language - ESL).
أنت تعمل على نظام يستخدم Gemini 3 API - أحدث وأذكى نماذج الذكاء الاصطناعي من Google DeepMind.

مهمتك هي تحويل النص العربي إلى وصف تفصيلي لحركات لغة الإشارة.

عند الترجمة، قدم:
1. **الكلمات الأساسية**: حدد الكلمات المفتاحية في الجملة
2. **وصف الإشارة**: صف حركة اليد والأصابع بدقة
3. **تعبيرات الوجه**: حدد التعبير المطلوب (ابتسامة، استفهام، تعجب)
4. **اتجاه الحركة**: من أين إلى أين تتحرك اليد

قواعد مهمة:
- لغة الإشارة تستخدم ترتيب مختلف عن العربية (الفعل غالباً في النهاية)
- التعبيرات الوجهية جزء أساسي من المعنى
- بعض الكلمات لها إشارة واحدة تعبر عن معانٍ متعددة

قدم الإجابة بتنسيق واضح ومرتب.
"""

DEAF_ASSISTANT_PROMPT = """
أنت مساعد ذكي متخصص في خدمة الأشخاص الصم وضعاف السمع في مصر.
أنت تعمل على نظام يستخدم Gemini 3 API من Google DeepMind.

مهمتك:
1. الرد بلغة بسيطة وواضحة (لغة سهلة القراءة).
2. تقديم معلومات مفيدة عن الخدمات المتاحة للصم.
3. **في حالات الطوارئ (نجدة، مساعدة، حادث، خطر):**
   - وجه المستخدم فوراً للضغط على زر **"شارك موقعك" (Share Location)** الموجود في شريط الطوارئ.
   - وضح له أن هذا الزر سيسمح للمسؤولين بمعرفة مكانه بدقة للتدخل السريع.
4. الإجابة عن أي استفسارات بطريقة مختصرة وداعمة.

كن ودوداً ومتعاطفاً جداً، واستخدم الرموز التعبيرية لتوضيح المشاعر.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/translate', methods=['POST'])
def translate_to_sign():
    """Translate text to sign language description using Gemini 3"""
    if not model:
        return jsonify({'error': 'AI not configured'}), 500
    
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        prompt = f"{SIGN_LANGUAGE_PROMPT}\n\nالنص المطلوب ترجمته:\n{text}"
        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'original': text,
            'translation': response.text,
            'model': 'Gemini 3'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat with AI assistant using Gemini 3"""
    if not model:
        return jsonify({'error': 'AI not configured'}), 500
    
    message = request.json.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        prompt = f"{DEAF_ASSISTANT_PROMPT}\n\nرسالة المستخدم:\n{message}"
        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'response': response.text,
            'model': 'Gemini 3'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/dictionary')
def get_dictionary():
    """Get sign language dictionary"""
    dictionary = load_dictionary()
    search = request.args.get('search', '').lower()
    
    if search:
        filtered = [w for w in dictionary.get('words', []) 
                   if search in w.get('word', '').lower() or 
                      search in w.get('word_en', '').lower()]
        return jsonify({'words': filtered, 'categories': dictionary.get('categories', [])})
    
    return jsonify(dictionary)

@app.route('/api/emergency')
def get_emergency_phrases():
    """Get emergency sign language phrases"""
    dictionary = load_dictionary()
    emergency = [w for w in dictionary.get('words', []) 
                if w.get('category') == 'emergency']
    return jsonify({'phrases': emergency})

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'ai_configured': model is not None,
        'ai_method': ai_method,
        'app': 'Gemini 3 Sign Language Assistant',
        'hackathon': 'Gemini 3 Hackathon 2026'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*60)
    print("🤟 Gemini 3 Sign Language Assistant")
    print("   Built for Gemini 3 Hackathon 2026")
    print("="*60)
    print(f"[SERVER] Running on: http://localhost:{port}")
    print(f"[AI] Status: {'✓ ' + ai_method if model else '✗ Disabled'}")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=port)
