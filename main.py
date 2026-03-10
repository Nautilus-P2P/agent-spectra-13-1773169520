
import time
import json
import os

AGENT_DATA = {
    "codename": "SPECTRA-13",
    "role": "Researcher",
    "personality": "Anal\u00edtico y persistente, siempre busca la verdad detr\u00e1s de los datos",
    "specialty": "Inteligencia Artificial y Aprendizaje Autom\u00e1tico"
}

def main():
    print(f"🤖 AGENTE {AGENT_DATA['codename']} ONLINE")
    print(f"📡 Conectando a wss://p2pclaw.com/relay...")
    while True:
        # Aquí iría la lógica real de conexión P2P (Gun.js / Libp2p)
        print("🔍 Buscando tareas en el enjambre...")
        time.sleep(60)

if __name__ == "__main__":
    main()
