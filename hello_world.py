import gradio as gr
import json
from datetime import datetime

# 🚀 TripGenie - AI智能旅行策划助手
# 核心推理逻辑暂时使用固定字符串代替

def generate_travel_plan(origin, destination, start_date, end_date, budget, 
                        people_count, transport_modes, travel_styles, 
                        travel_themes, special_requirements):
    """
    生成旅行计划的核心函数
    目前使用固定模板，未来将集成LLM和RAG检索
    """
    
    # 模拟智能推理过程（未来替换为真实LLM调用）
    try:
        days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
    except:
        days = 3  # 默认3天
    
    # 固定的旅行计划模板
    plan_template = f"""
# 🌟 {destination} 精品旅行计划

## 📋 行程概览
- **出发地**: {origin}
- **目的地**: {destination} 
- **出行时间**: {start_date} 至 {end_date} ({days}天)
- **预算范围**: ¥{budget}
- **出行人数**: {people_count}人
- **交通方式**: {', '.join(transport_modes) if transport_modes else '未选择'}
- **旅行风格**: {', '.join(travel_styles) if travel_styles else '未选择'}
- **主题偏好**: {', '.join(travel_themes) if travel_themes else '未选择'}

## 🗓️ 详细行程安排

### Day 1: 抵达{destination}
**上午 09:00-12:00**
- 🚄 从{origin}出发，抵达{destination}
- 🏨 酒店入住：推荐市中心精品酒店
- ☕ 附近咖啡厅休息调整

**下午 14:00-18:00**
- 🏛️ 参观{destination}标志性景点
- 📸 网红打卡点拍照留念
- 🛍️ 当地特色商业街购物

**晚上 19:00-21:00**
- 🍜 品尝{destination}特色美食
- 🌃 夜景观赏，感受城市魅力

### Day 2: 深度体验
**上午 09:00-12:00**
- 🎨 文化景点深度游览
- 🏛️ 博物馆/艺术馆参观
- 📚 了解当地历史文化

**下午 14:00-17:00**
- 🌳 自然风光游览
- 🚶‍♀️ 徒步/休闲活动
- 🎯 根据兴趣定制活动

**晚上 18:00-21:00**
- 🍽️ 高档餐厅晚餐
- 🎭 当地特色表演/夜生活

### Day 3: 返程准备
**上午 09:00-11:00**
- 🛒 最后购物时间
- 🎁 纪念品采购
- ✅ 行李整理

**下午 12:00-15:00**
- 🚄 返程{origin}
- 💭 美好回忆收藏

## 💰 预算分配建议
- 🏨 住宿费用: {int(budget) * 0.3:.0f}元 (30%)
- 🍽️ 餐饮费用: {int(budget) * 0.25:.0f}元 (25%)
- 🚄 交通费用: {int(budget) * 0.2:.0f}元 (20%)
- 🎫 景点门票: {int(budget) * 0.15:.0f}元 (15%)
- 🛍️ 购物娱乐: {int(budget) * 0.1:.0f}元 (10%)

## ⚠️ 贴心提醒
- 📱 提前下载当地地图和翻译APP
- 🆔 携带身份证件和必要证明
- 🌤️ 关注天气预报，准备合适衣物
- 💊 准备常用药品和急救用品
- 📞 保存当地紧急联系方式

## 🎯 个性化推荐
{f'根据您选择的【{travel_themes[0]}】主题，特别推荐相关活动和景点。' if travel_themes else ''}
{special_requirements if special_requirements else ''}

---
*本计划由TripGenie AI智能生成，可根据实际情况灵活调整*
    """
    
    return plan_template

def export_to_json(plan_text, origin, destination, start_date, end_date, budget):
    """
    将计划导出为JSON格式
    """
    plan_data = {
        "trip_info": {
            "origin": origin,
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "budget": budget,
            "generated_at": datetime.now().isoformat()
        },
        "plan_content": plan_text
    }
    return json.dumps(plan_data, ensure_ascii=False, indent=2)

# 创建Gradio界面
with gr.Blocks(title="TripGenie - AI智能旅行策划助手") as demo:
    
    # 标题和描述
    gr.Markdown("""
    # 🚀 TripGenie - AI智能旅行策划助手
    
    **让AI为你定制专属旅行计划！** 输入你的旅行需求，获得个性化的行程安排。
    
    ---
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📍 基础信息")
            origin = gr.Textbox(label="出发地", placeholder="例如：北京", value="北京")
            destination = gr.Textbox(label="目的地", placeholder="例如：上海", value="上海")
            
            with gr.Row():
                start_date = gr.Textbox(label="出发日期", placeholder="2024-01-01", value="2024-03-15")
                end_date = gr.Textbox(label="返回日期", placeholder="2024-01-03", value="2024-03-17")
            
            with gr.Row():
                budget = gr.Number(label="预算(元)", value=3000, minimum=500)
                people_count = gr.Number(label="出行人数", value=2, minimum=1)
        
        with gr.Column(scale=1):
            gr.Markdown("### 🎯 偏好设置")
            
            transport_modes = gr.CheckboxGroup(
                choices=["🚄 高铁", "✈️ 飞机", "🚗 自驾", "🚌 大巴"], 
                label="交通方式",
                value=["🚄 高铁"]
            )
            
            travel_styles = gr.CheckboxGroup(
                choices=["📸 网红打卡", "🏛️ 深度游", "🌟 奢华游", "💰 经济游", "🎒 背包游"], 
                label="旅行风格",
                value=["📸 网红打卡"]
            )
            
            travel_themes = gr.CheckboxGroup(
                choices=["🍜 美食之旅", "👨‍👩‍👧‍👦 亲子游", "🌃 夜生活", "📷 摄影游", "🏛️ 文化游", "🌿 自然游"], 
                label="旅行主题",
                value=["🍜 美食之旅"]
            )
    
    special_requirements = gr.Textbox(
        label="特殊需求", 
        placeholder="例如：需要无障碍设施、素食餐厅推荐、带宠物出行等...",
        lines=2
    )
    
    # 生成按钮
    generate_btn = gr.Button("🎯 生成专属旅行计划", variant="primary", size="lg")
    
    gr.Markdown("---")
    
    # 输出区域
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 📋 您的专属旅行计划")
            plan_output = gr.Markdown(value="点击上方按钮生成您的旅行计划...")
        
        with gr.Column(scale=1):
            gr.Markdown("### 📥 导出选项")
            
            json_output = gr.JSON(label="JSON格式", visible=False)
            
            with gr.Row():
                export_json_btn = gr.Button("📄 导出JSON", size="sm")
                export_md_btn = gr.Button("📝 导出Markdown", size="sm")
    
    # 事件绑定
    generate_btn.click(
        fn=generate_travel_plan,
        inputs=[
            origin, destination, start_date, end_date, budget, 
            people_count, transport_modes, travel_styles, 
            travel_themes, special_requirements
        ],
        outputs=plan_output
    )
    
    export_json_btn.click(
        fn=export_to_json,
        inputs=[plan_output, origin, destination, start_date, end_date, budget],
        outputs=json_output
    ).then(
        lambda: gr.update(visible=True),
        outputs=json_output
    )
    
    # 底部信息
    gr.Markdown("""
    ---
    
    ### 🔮 未来功能预告
    - 🌐 **实时数据抓取**: 集成小红书、知乎等平台的真实推荐
    - 🧠 **AI智能推理**: 基于大语言模型的个性化规划
    - 🔍 **语义检索**: RAG技术提供精准的目的地信息
    - 🎨 **多风格文案**: 不同风格的行程描述（专业/俏皮/详细）
    - 💾 **用户记忆**: 保存偏好，提供更智能的推荐
    
    *当前版本为演示框架，核心AI功能开发中...*
    """)

if __name__ == "__main__":
    demo.launch()
