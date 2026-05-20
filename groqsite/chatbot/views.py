
from django.shortcuts import render
from django.http import JsonResponse
from groq import Groq  
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

from django.shortcuts import render

def index(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        return render(request, 'chatbot/index.html', {'user_input': user_input})
    else:
        return render(request, 'chatbot/index.html')

def ask(request):
    user_msg = request.GET.get("message", "")
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_msg}
            ]
        )
        answer = response.choices[0].message.content
        return JsonResponse({'reply': answer})  # ✅ This must be a JSON dict
    except Exception as e:
        return JsonResponse({'reply': f"Error: {str(e)}"})
