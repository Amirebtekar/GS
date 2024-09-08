import streamlit as st
import requests
import xml.etree.ElementTree as ET

def fetch_suggestions(query):
    # ارسال درخواست به API
    url = f"https://suggestqueries.google.com/complete/search?q={query}&client=toolbar&hl=IR"
    response = requests.get(url)
    
    # تجزیه محتوای XML
    root = ET.fromstring(response.content)
    
    # استخراج پیشنهادات
    suggestions = [suggestion.attrib['data'] for suggestion in root.findall('.//suggestion')]
    return suggestions

def main():
    # گرفتن کوئری از کاربر
    query = st.text_input("لطفا کلمه مورد نظر را وارد کنید:", "")
    
    if query:
        # درخواست به API و دریافت پیشنهادات
        suggestions = fetch_suggestions(query)
        
        # نمایش پیشنهادات در Streamlit
        st.write("پیشنهادات:")
        for suggestion in suggestions:
            st.write(suggestion)

        # تکرار برای هر پیشنهاد و دریافت پیشنهادات جدید
        for suggestion in suggestions:
            st.write(f"پیشنهادات برای '{suggestion}':")
            new_suggestions = fetch_suggestions(suggestion)
            for new_suggestion in new_suggestions:
                st.write(new_suggestion)

if __name__ == "__main__":
    main()
