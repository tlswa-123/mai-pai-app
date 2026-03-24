# MaiPal APP 系统架构（v1.2.2）

## 图1：系统架构图（整体技术视图）

```mermaid
graph TB
    subgraph 用户端
        A[Flutter APP\n(3 Tab: 对话 / 总结计划 / 中医馆)] --> B[数字人界面\n(Lottie / Rive 动画)]
    end

    subgraph 多模态输入层
        B --> C1[文字 / 语音输入\n(问 + 闻)]
        B --> C2[摄像头自动拍照\n(望)]
        B --> C3[手机健康 App 数据\n(切：心率 / 睡眠)]
    end

    C1 & C2 & C3 --> D[AI Agent\n(简单 Python 节点式)]

    subgraph 核心后端
        D --> E[Qwen LLM]
        D --> F[PDF 直接读取\n(中医典籍)]
        D --> G[SQLite / PostgreSQL\n(用户 Profile + 聊天记录 + 报告 + 计划)]
    end

    subgraph 人机协同层
        D --> H[专家 double-check 占位\n(高风险异步审核)]
        H --> I[反馈 → 更新长期画像]
    end

    I --> G
    D --> B[返回自然对话结果]
    
    style D fill:#e3f2fd
    style H fill:#fff3e0
```
