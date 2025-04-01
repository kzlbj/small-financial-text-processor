# 小型金融文本处理应用

这是一个使用 Flask 和 NLTK 构建的 RESTful API，用于分析金融文本并返回前 10 个最常见的金融关键词及其频率。应用现已支持中英文文本处理，适用于年报审核、文档索引和合规检查，目标用户包括金融分析师、合规官和金融机构。

## 目录

- [设置说明](#设置说明)
- [API 使用](#api-使用)
- [测试方法](#测试方法)
- [错误处理](#错误处理)
- [项目结构](#项目结构)
- [限制](#限制)
- [许可](#许可)
- [贡献指南](#贡献指南)
- [部署](#部署)
- [维护](#维护)
- [联系方式](#联系方式)

## 设置说明

### 系统要求

- Python 3.6 或更高版本
- 互联网连接（用于下载 NLTK 数据）

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python app.py
```

应用将在 http://127.0.0.1:5000 上运行。

### 故障排除

- **NLTK 下载问题**：如果 NLTK 数据下载失败，请尝试手动下载：
  ```python
  import nltk
  nltk.download('stopwords')
  ```
  
- **环境变量**：设置 `FLASK_ENV=development` 开启调试模式

## API 使用

### 分析文本端点

- **URL**: `/analyze_text`
- **方法**: `POST`
- **内容类型**: `application/json`
- **速率限制**: 100 次/分钟（计划中）
- **认证**: 基本认证（计划中）

#### 请求参数验证

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 是 | 要分析的文本，英文或中文 |

#### 英文请求示例

```json
{
  "text": "This is a financial report about stock market performance and bond yields. The equity market showed strong performance while corporate bonds experienced volatility due to interest rate fluctuations. Investors are concerned about inflation and its impact on their investment portfolio."
}
```

#### 英文响应示例

```json
[
  {"word": "market", "frequency": 2},
  {"word": "stock", "frequency": 1},
  {"word": "bond", "frequency": 1},
  {"word": "equity", "frequency": 1},
  {"word": "interest", "frequency": 1},
  {"word": "investment", "frequency": 1},
  {"word": "portfolio", "frequency": 1},
  {"word": "inflation", "frequency": 1}
]
```

#### 中文请求示例

```json
{
  "text": "这是一份关于股票市场表现和债券收益率的金融报告。股权市场表现强劲，而公司债券因利率波动而经历波动。投资者担忧通货膨胀及其对投资组合的影响。"
}
```

#### 中文响应示例

```json
[
  {"word": "股票", "frequency": 1},
  {"word": "市场", "frequency": 2},
  {"word": "债券", "frequency": 1},
  {"word": "股权", "frequency": 1},
  {"word": "利率", "frequency": 1},
  {"word": "投资", "frequency": 1},
  {"word": "投资组合", "frequency": 1},
  {"word": "通货膨胀", "frequency": 1}
]
```

## 测试方法

### 使用 curl 测试

#### 英文测试

```bash
curl -X POST https://your-api-domain.com/analyze_text \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a financial report about stock market performance and bond yields."}'
```

#### 中文测试

```bash
curl -X POST https://your-api-domain.com/analyze_text \
  -H "Content-Type: application/json" \
  -d '{"text": "这是一份关于股票市场表现和债券收益率的金融报告。"}'
```

### 使用 Postman 测试

1. 打开 Postman
2. 创建新的 POST 请求，URL 设为 `http://127.0.0.1:5000/analyze_text`
3. 在 Headers 选项卡中，添加 `Content-Type: application/json`
4. 在 Body 选项卡中，选择 raw 格式，并输入 JSON
5. 点击发送按钮

[查看 Postman 测试教程](https://your-tutorial-link.com)

## 错误处理

| 状态码 | 说明 | 示例响应 |
|--------|------|----------|
| 400 | 未提供文本或文本为空 | `{"error": "No text provided"}` |
| 500 | 服务器内部错误 | `{"error": "处理文本时出错: [详细错误]"}` |

## 项目结构

```
financial-text-processor/
├── app.py                 # Flask应用和API端点
├── text_processor.py      # 文本处理逻辑和关键词列表
├── requirements.txt       # 项目依赖
└── README.md              # 项目文档
```

## 限制

- 仅支持预定义的金融关键词列表中的词语识别
- 可能无法捕获所有专业术语或新兴金融术语
- 简化的中文停用词列表，可能需要根据具体用例扩展

## 许可

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 部署

### Heroku 部署

```bash
# 安装Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
```

### Docker 部署

```bash
docker build -t financial-text-processor .
docker run -p 5000:5000 financial-text-processor
```

## 维护

- 定期更新依赖包
- 扩展金融关键词列表
- 改进文本处理算法

## 联系方式

如有问题或建议，请联系 kyriezo@163.com

---

# Small Financial Text Processing Application

This is a RESTful API built with Flask and NLTK for analyzing financial texts and returning the top 10 most common financial keywords and their frequencies. The application now supports both Chinese and English text processing. It is suitable for annual report reviews, document indexing, and compliance checks, targeted at financial analysts, compliance officers, and financial institutions.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Testing Methods](#testing-methods)
- [Error Handling](#error-handling)
- [Project Structure](#project-structure)
- [Limitations](#limitations)
- [License](#license)
- [Contributing](#contributing)
- [Deployment](#deployment)
- [Maintenance](#maintenance)
- [Contact](#contact)

## Setup Instructions

### System Requirements

- Python 3.6 or higher
- Internet connection (for downloading NLTK data)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Application

```bash
python app.py
```

The application will run on http://127.0.0.1:5000.

### Troubleshooting

- **NLTK Download Issues**: If NLTK data download fails, try downloading manually:
  ```python
  import nltk
  nltk.download('stopwords')
  ```
  
- **Environment Variables**: Set `FLASK_ENV=development` to enable debug mode

## API Usage

### Analyze Text Endpoint

- **URL**: `/analyze_text`
- **Method**: `POST`
- **Content Type**: `application/json`
- **Rate Limit**: 100 requests/minute (planned)
- **Authentication**: Basic auth (planned)

#### Request Parameter Validation

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| text | string | Yes | Text to analyze, English or Chinese |

#### English Request Example

```json
{
  "text": "This is a financial report about stock market performance and bond yields. The equity market showed strong performance while corporate bonds experienced volatility due to interest rate fluctuations. Investors are concerned about inflation and its impact on their investment portfolio."
}
```

#### English Response Example

```json
[
  {"word": "market", "frequency": 2},
  {"word": "stock", "frequency": 1},
  {"word": "bond", "frequency": 1},
  {"word": "equity", "frequency": 1},
  {"word": "interest", "frequency": 1},
  {"word": "investment", "frequency": 1},
  {"word": "portfolio", "frequency": 1},
  {"word": "inflation", "frequency": 1}
]
```

#### Chinese Request Example

```json
{
  "text": "这是一份关于股票市场表现和债券收益率的金融报告。股权市场表现强劲，而公司债券因利率波动而经历波动。投资者担忧通货膨胀及其对投资组合的影响。"
}
```

#### Chinese Response Example

```json
[
  {"word": "股票", "frequency": 1},
  {"word": "市场", "frequency": 2},
  {"word": "债券", "frequency": 1},
  {"word": "股权", "frequency": 1},
  {"word": "利率", "frequency": 1},
  {"word": "投资", "frequency": 1},
  {"word": "投资组合", "frequency": 1},
  {"word": "通货膨胀", "frequency": 1}
]
```

## Testing Methods

### Testing with curl

#### English Test

```bash
curl -X POST https://your-api-domain.com/analyze_text \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a financial report about stock market performance and bond yields."}'
```

#### Chinese Test

```bash
curl -X POST https://your-api-domain.com/analyze_text \
  -H "Content-Type: application/json" \
  -d '{"text": "这是一份关于股票市场表现和债券收益率的金融报告。"}'
```

### Testing with Postman

1. Open Postman
2. Create a new POST request with URL `http://127.0.0.1:5000/analyze_text`
3. Add `Content-Type: application/json` in the Headers tab
4. Select raw format in the Body tab and enter your JSON
5. Click the Send button

[View Postman Testing Tutorial](https://your-tutorial-link.com)

## Error Handling

| Status Code | Description | Example Response |
|-------------|-------------|------------------|
| 400 | No text provided or empty text | `{"error": "No text provided"}` |
| 500 | Server internal error | `{"error": "Error processing text: [detailed error]"}` |

## Project Structure

```
financial-text-processor/
├── app.py                 # Flask application and API endpoints
├── text_processor.py      # Text processing logic and keyword lists
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Limitations

- Only recognizes words from predefined financial keyword lists
- May not capture all specialized terminology or emerging financial terms
- Simplified Chinese stopwords list, might need expansion for specific use cases

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Deployment

### Heroku Deployment

```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
```

### Docker Deployment

```bash
docker build -t financial-text-processor .
docker run -p 5000:5000 financial-text-processor
```

## Maintenance

- Regularly update dependencies
- Expand financial keyword lists
- Improve text processing algorithms

## Contact

For questions or suggestions, please contact kyriezo@163.com
