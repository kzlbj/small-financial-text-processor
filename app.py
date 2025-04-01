from flask import Flask, request, jsonify
import text_processor

app = Flask(__name__)

@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    data = request.get_json()
    
    if not data or 'text' not in data or not data['text'].strip():
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    print(f"接收到文本进行分析: {text[:100]}...")  # 只打印前100个字符
    
    try:
        result = text_processor.process_text(text)
        print(f"分析结果: {result}")
        return jsonify(result)
    except Exception as e:
        print(f"处理文本时出错: {str(e)}")
        return jsonify({"error": f"处理文本时出错: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False) 