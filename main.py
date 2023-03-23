import streamlit as st
import openai
import time
import streamlit.components.v1 as components

def main():

    
    st.set_page_config(
        page_title='p[AI]tch',
        initial_sidebar_state='collapsed',
        page_icon='📈',
        layout="wide")

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    def twitter_follow_button(username):
        follow_button = f'<a href="https://twitter.com/{username}?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">@{username}</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
        return follow_button
    
    donate = '''<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="UF6NAEW2NCQN2" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_IT/i/scr/pixel.gif" width="1" height="1" />
</form>
'''
    
    s,t,q,r,z = st.columns([1,2,6,3,1])
    with t:
        st.header('📈 p[AI]tch:')
    with q:
        st.subheader('a comparison on the effort to build something with AI a year ago VS')
    with r:
    # Add content to the footer container
        st.markdown('<div style="text-align: left">chek the code at <a href="https://github.com/klein-t">klein-t/p[AI]tch</a></div>', unsafe_allow_html=True)
# Create the follow button
        twitter_handle = "KleinTahiraj"
        st.markdown(f'follow me on Twitter {twitter_follow_button(twitter_handle)}', unsafe_allow_html=True)
        ll,rr = st.columns([10,9], gap = 'small')
        with ll:
            st.markdown(f'or buy me a coffee', unsafe_allow_html=True)
        with rr:
            st.markdown(donate, unsafe_allow_html=True)
            
    st.markdown("""---""")
    x, uno, due, y = st.columns([1,4,4,1], gap='medium')
    with uno:
        st.subheader('ONE YEAR AGO...')
        st.write('...get the scripts for 1,000 hours of pitches. Clean them. Select the model, likely BERT or GPT-2. Format training data. Fine-tune the model. Wait. Give the model a prompt. Prey. Get a funny (not on purpose) but incoherent output :p')
        
    with due:
        st.subheader('NOW...')
        st.write('...write a 30-line prompt with some instructions and some examples. Give it to a LLM. Get a funny (on purpose) and coherent output c:')
        
        

    n, left, right, m = st.columns(spec = [1,4,4,1], gap = 'medium')

    with left:
        st.write('ESTIMATED TIME: days')
        st.markdown("""---""")
        
        tweet = """
                <blockquote class="twitter-tweet" style="float:right; width:500px;">
                <p lang="en" dir="ltr">I forced a bot to watch over 1,000 hours of startup pitch meetings and then asked it to re-create a startup pitch meeting of its own. Here is the first page. <a href="https://t.co/BK1yBZ2EB2">pic.twitter.com/BK1yBZ2EB2</a></p>&mdash; Roshan Patel (@roshanpateI) <a href="https://twitter.com/roshanpateI/status/1476620230692679680?ref_src=twsrc%5Etfw">December 30, 2021</a>
                </blockquote>
                <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                """
        components.html(tweet, height=900)

    with right:
        st.write('ESTIMATED TIME: 20 minutes')
        st.markdown("""---""")

        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt_path = 'prompt.txt'
        with open(prompt_path, "r", encoding="utf-8") as prompt:
            template = prompt.read()

        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.93,
            messages=[
                {"role": "system", "content": template},
                {"role": "user", "content": "\n \n  # NOW IS YOUR TURN### Script: "},
            ],
        )
        message = output["choices"][0]["message"]["content"]
        output_elem = st.empty()

        stream_message=''
        for char in message:
            stream_message = stream_message + char
            output_elem.markdown(
                f'<div style="text-align: justify;">{stream_message}</div>', unsafe_allow_html=True)
            time.sleep(0.001)
        
    

if __name__ == "__main__":
    main()
