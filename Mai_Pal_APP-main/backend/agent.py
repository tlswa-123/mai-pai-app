from dotenv import load_dotenv
load_dotenv()

class MaiPalAgent:
    def __init__(self):
        self.user_profile = {}      # 长期画像
        self.chat_history = []
        self.expert_review_status = "pending"  # double-check 占位

    # ==================== 节点（严格按 README 封装） ====================
    def input_processor(self, text: str = None, image_bytes: bytes = None, voice_text: str = None, health_data: dict = None):
        """多模态预处理节点"""
        return {
            "text": text or "",
            "image": image_bytes,
            "voice": voice_text or "",
            "health": health_data or {}
        }

    def observation_node(self, image_bytes: bytes):
        """望节点：气色分析（MVP 用 Qwen 描述图片）"""
        # TODO: 调用 Qwen Vision 分析气色
        return "气色偏淡，精神状态一般"

    def voice_node(self, voice_text: str):
        """闻节点：声音语气分析"""
        # TODO: 简单语气判断，后续加音频特征
        return "声音平稳，情绪较放松"

    def pulse_node(self, health_data: dict):
        """切节点：读取手机健康 App 数据"""
        heart_rate = health_data.get("heart_rate", 75)
        sleep_hours = health_data.get("sleep_hours", 7)
        return f"心率 {heart_rate} bpm，睡眠 {sleep_hours} 小时"

    def question_node(self, user_input: str):
        """问节点：自然对话 + Qwen 回复"""
        # TODO: 调用 Qwen 生成自然陪伴式回复
        return f"脉脉收到：{user_input}，我来帮你分析一下～"

    def expert_review_node(self, diagnosis: dict):
        """专家 double-check 占位节点"""
        # MVP 阶段模拟返回
        self.expert_review_status = "approved"
        return diagnosis

    def output_node(self, combined_data: dict):
        """输出节点：生成报告 + 计划"""
        report = "检测报告：气血较弱，建议温补"
        plan = "今日计划：早睡 + 红枣粥"
        return {
            "report": report,
            "plan": plan,
            "expert_status": self.expert_review_status,
            "updated_profile": self.user_profile
        }

    # ==================== 主流程 ====================
    def process_conversation(self, user_input: str, image_bytes=None, voice_text=None, health_data=None):
        """完整一次对话流程"""
        inputs = self.input_processor(user_input, image_bytes, voice_text, health_data)
        
        obs = self.observation_node(inputs["image"]) if inputs["image"] else ""
        voi = self.voice_node(inputs["voice"])
        pul = self.pulse_node(inputs["health"])
        que = self.question_node(inputs["text"])
        
        diagnosis = {"observation": obs, "voice": voi, "pulse": pul, "question": que}
        reviewed = self.expert_review_node(diagnosis)
        
        return self.output_node(reviewed)
