import requests
import os
from flask import Flask, request, jsonify
from urllib.parse import parse_qs
from dotenv import load_dotenv


app = Flask(__name__)

# Настройки AmoCRM
AMOCRM_DOMAIN = os.getenv("AMOCRM_DOMAIN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CUSTOM_FIELD_ID = os.getenv("CUSTOM_FIELD_ID")
VALUE = "test"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Получаем данные в виде строки
        data = request.get_data(as_text=True)
        
        # Декодируем URL-кодированные параметры
        parsed_data = parse_qs(data)
        
        # Преобразуем в JSON
        json_data = {key: value[0] if len(value) == 1 else value for key, value in parsed_data.items()}
        print("Parsed Data:", json_data)

        # Проверяем наличие lead_id
        lead_id = json_data.get("unsorted[add][0][lead_id]")
        client_id = json_data.get("unsorted[add][0][source_data][client][id]")
        print(f"Lead ID: {lead_id}, Client ID: {client_id}")
        
        if not lead_id:
            return jsonify({"error": "lead_id not found"}), 400

        # Формируем URL запроса
        url = f"https://{AMOCRM_DOMAIN}/api/v4/leads/{lead_id}"
        print(f"URL for PATCH request: {url}")

        # Заголовки
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        print("Headers:", headers)

        # Данные для обновления
        payload = {
            "custom_fields_values": [
                {
                    "field_id": CUSTOM_FIELD_ID,
                    "values": [{"value": client_id}]
                }
            ]
        }
        print("Payload:", payload)

        # Отправка запроса
        response = requests.patch(url, json=payload, headers=headers)
        result = response.json()
        print(f"Response Status: {response.status_code}, Response: {result}")

        return jsonify({"status": response.status_code, "response": result}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
