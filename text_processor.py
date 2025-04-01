import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
import jieba  # 添加结巴分词库用于中文分词

# 下载停用词数据（只需下载一次）
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# 金融关键词列表（英文）
FINANCIAL_KEYWORDS_EN = [
    'stock', 'bond', 'fund', 'market', 'asset', 'liability', 'revenue', 
    'profit', 'loss', 'equity', 'debt', 'interest', 'tax', 'investment', 
    'dividend', 'credit', 'debit', 'income', 'expense', 'cash', 'portfolio', 
    'option', 'future', 'commodity', 'currency', 'inflation', 'deflation', 
    'recession', 'boom', 'bear', 'bull', 'bubble', 'crash', 'merger', 
    'acquisition', 'IPO', 'divestiture', 'audit', 'compliance', 'regulation', 
    'SEC', 'FASB', 'GAAP', 'IFRS'
]

# 金融关键词列表（中文）
FINANCIAL_KEYWORDS_CN = [
    '股票', '债券', '基金', '市场', '资产', '负债', '收入', 
    '利润', '亏损', '股权', '债务', '利息', '税', '投资', 
    '股息', '信用', '借记', '收益', '支出', '现金', '投资组合', 
    '期权', '期货', '商品', '货币', '通货膨胀', '通货紧缩', 
    '经济衰退', '繁荣', '熊市', '牛市', '泡沫', '崩盘', '合并', 
    '收购', '首次公开募股', '剥离', '审计', '合规', '监管', 
    '证监会', '财会准则委员会', '通用会计准则', '国际财务报告准则'
]

# 中文停用词列表（简化版）
CHINESE_STOP_WORDS = [
    '的', '了', '和', '是', '在', '我', '有', '不', '这', '人', 
    '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', 
    '你', '会', '着', '没有', '看', '好', '自己', '这个'
]

def is_chinese(text):
    """
    判断文本是否主要包含中文字符
    """
    # 检查是否包含中文字符
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return len(chinese_chars) > len(text) / 4  # 如果中文字符占比超过25%，认为是中文文本

def process_text(text):
    """
    处理输入文本并返回前10个最常见的金融关键词及其频率
    
    参数:
        text (str): 需要分析的文本
        
    返回:
        list: 包含字典的列表，每个字典有'word'和'frequency'键
    """
    # 检测是否为中文文本
    is_cn_text = is_chinese(text)
    print(f"文本类型检测: {'中文' if is_cn_text else '英文'}")
    
    # 转换为小写（对英文有效）
    text = text.lower() if not is_cn_text else text
    
    # 移除标点符号
    text = re.sub(r'[^\w\s]', '', text) if not is_cn_text else re.sub(r'[^\u4e00-\u9fff\w\s]', '', text)
    
    # 分词
    if is_cn_text:
        # 使用jieba进行中文分词
        words = list(jieba.cut(text))
        print(f"中文分词结果(前20个): {words[:20]}")
        # 移除中文停用词
        words = [word for word in words if word not in CHINESE_STOP_WORDS and len(word.strip()) > 0]
        # 仅保留中文金融关键词
        financial_words = [word for word in words if word in FINANCIAL_KEYWORDS_CN]
        print(f"找到的中文金融关键词: {financial_words}")
    else:
        # 英文分词
        words = text.split()
        print(f"英文分词结果(前20个): {words[:20]}")
        # 移除英文停用词
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words and len(word.strip()) > 0]
        # 仅保留英文金融关键词
        financial_words = [word for word in words if word in FINANCIAL_KEYWORDS_EN]
        print(f"找到的英文金融关键词: {financial_words}")
    
    # 计算词频
    word_counts = Counter(financial_words)
    
    # 获取前10个最常见的词
    top_words = word_counts.most_common(10)
    
    # 格式化结果
    result = [{"word": word, "frequency": freq} for word, freq in top_words]
    
    # 如果没有找到任何金融关键词，返回一个特定的消息
    if not result:
        return [{"message": "未找到任何金融关键词", "suggestion": "请尝试使用包含更多金融术语的文本"}]
    
    return result 