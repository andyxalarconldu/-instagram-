import requests
import time
import random

def extract_username(input_text):
    if input_text and "instagram.com" in input_text:
        return input_text.rstrip("/").split("/")[-1].split("?")[0]
    return input_text.strip().lower()

def get_instagram_data(input_text):
    username = extract_username(input_text)
    print(f"📡 Iniciando conexión mediante IP Móvil para: @{username}...")

    # --- TUS COOKIES (Cópialas de tu navegador) ---
    cookies = {
        'sessionid': '48136707565%3AeLL5DnkMs8NeqN%3A2%3AAYgvQCRZBSPfPJlAzKVzBfTGDHvp0csMfYuKAB4fZQ',
        'csrftoken': 'IyrgFBmZKcM19gkgJxzhrjiaOOWLhJqg',
    }

    # Cabeceras que emulan un navegador real al 100%
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '129477',
        'X-CSRFToken': 'IyrgFBmZKcM19gkgJxzhrjiaOOWLhJqg',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': f'https://www.instagram.com/{username}/',
    }

    try:
        # Pausa aleatoria para simular comportamiento humano antes de pedir datos
        time.sleep(random.uniform(2, 4))
        
        # Endpoint de API que usa Instagram Web para cargar perfiles
        api_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
        
        response = requests.get(api_url, headers=headers, cookies=cookies, timeout=15)
        
        if response.status_code != 200:
            print(f"❌ El servidor respondió con error {response.status_code}. Revisa tus cookies.")
            return None

        data = response.json()['data']['user']
        print(f"✅ Conexión exitosa. Extrayendo datos reales de @{username}...")

        result = {
            "username": data['username'],
            "full_name": data['full_name'],
            "biography": data['biography'],
            "followers": data['edge_followed_by']['count'],
            "following": data['edge_follow']['count'],
            "profile_pic": data['profile_pic_url_hd'],
            "posts": []
        }

        # Extraemos exactamente los posts reales del JSON
        edges = data['edge_owner_to_timeline_media']['edges']
        for i, edge in enumerate(edges):
            if i >= 10: break # Aquí defines si quieres 6 o 10
            node = edge['node']
            
            # Buscamos el texto del post
            caption = ""
            if node['edge_media_to_caption']['edges']:
                caption = node['edge_media_to_caption']['edges'][0]['node']['text'][:60] + "..."

            result["posts"].append({
                "caption": caption if caption else "Publicación de Instagram",
                "likes": f"{node['edge_liked_by']['count']:,}",
                "comments": f"{node['edge_media_to_comment']['count']:,}",
                "image": node['display_url'],
                "url": f"https://www.instagram.com/p/{node['shortcode']}/"
            })
        
        print(f"📸 ¡Éxito! Se obtuvieron {len(result['posts'])} publicaciones reales.")
        return result

    except Exception as e:
        print(f"❌ Error en la extracción: {e}")
        return None