import streamlit as st
from project1后端代码 import generate_script
# 生成大标题
st.title("🎬 视频脚本生成器")

#生成侧边栏
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    # markdown语法
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

# 分别输入主题，时长和滑块形式的创造力
subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏱️ 请输入视频的大致时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)

# 按钮形式
submit = st.button("生成脚本")

#点了按钮之后先检查前面所有内容是否已经输入
if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    #立即停止所有后续代码的执行，包括条件语句后所有语句的执行
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    # 加载组件，没加载出来之前会一直显示在加载
    with st.spinner("AI正在思考中，请稍等..."):
        search_result, title, script = generate_script(subject, video_length, creativity, openai_api_key)
        #st.success("视频脚本已生成！") 是 Streamlit 中的一个函数调用，用于在应用中显示一个带有绿色背景的成功消息。这个消息用于通知用户某个操作已成功完成。
        #具体来说，这一行代码会在 Streamlit 应用界面上显示一条成功提示，内容为“视频脚本已生成！”，告知用户视频脚本已经生成成功。
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)
    # 折叠展开组件
    with st.expander("维基百科搜索结果 👀"):
        st.info(search_result)



#st.info(search_result) 和 st.write(search_result) 是 Streamlit 库中用于显示信息的两种不同方法。它们之间的区别在于信息的显示方式和用途：

# st.info(search_result)：
# 用于显示带有蓝色背景的提示信息。
# 一般用于传达信息、通知或其他非错误的状态更新。
#
# st.write(search_result)：
# 用于显示任意的文本、数据框、图表、或其他数据类型。
# 更通用，适用于显示任何需要的内容。
# 显示效果：以默认样式展示传入的内容，没有特定的背景颜色。



#区别：第一种方式使用了 st.stop()，这会立即停止所有后续代码的执行。第二种方式使用了 elif，一旦找到匹配的条件，它会跳过后续的条件检查，但会继续执行其后的代码。
# if submit and not openai_api_key:
#     st.info("请输入你的OpenAI API密钥")
#
# elif submit and not subject:
#     st.info("请输入视频的主题")
#
# elif submit and not video_length >= 0.1:
#     st.info("视频长度需要大于或等于0.1")
# 和
# if submit and not openai_api_key:
#     st.info("请输入你的OpenAI API密钥")
#     st.stop()
# if submit and not subject:
#     st.info("请输入视频的主题")
#     st.stop()
# if submit and not video_length >= 0.1:
#     st.info("视频长度需要大于或等于0.1")
#     st.stop()



# st.subheader("🔥 标题：") 和 st.title("🔥 标题：") 是 Streamlit 中用于显示标题文本的两种不同方法，它们之间的区别在于文本的格式和大小。

# st.subheader("🔥 标题：")
# 功能：显示一个子标题。
# 效果：子标题通常比主标题小，但比普通文本大。适用于页面的次级标题，组织内容层次结构。
#
# st.title("🔥 标题：")
# 功能：显示一个主标题。
# 效果：主标题通常是页面上最大的文本，用于页面或内容的主要标题。