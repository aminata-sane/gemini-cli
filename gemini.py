import sys
import os
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    console = Console()
    console.print("[bold red]Erreur : GEMINI_API_KEY n'est pas défini dans les variables d'environnement.[/bold red]")
    sys.exit(1)
client = genai.Client(api_key=api_key)
console = Console()

def main():
    prompt = " ".join(sys.argv[1:])
    if not prompt:
        console.print("[bold red]Usage:[/bold red] gemini \"votre question\"")
        return

    # Animation de chargement
    with console.status("[bold blue]Gemini réfléchit...", spinner="dots"):
        try:
            # Afficher l'entrée utilisateur
            console.print(f"\n[bold green]── User Input ──[/bold green]")
            console.print(Panel(prompt, border_style="green", expand=False))
            
            # On utilise le mode stream pour l'effet Copilot
            response_stream = client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            full_text = ""
            console.print("\n[bold cyan]── Gemini Copilot ──[/bold cyan]")
            
            # Affichage dynamique
            with Live(console=console, refresh_per_second=10) as live:
                for chunk in response_stream:
                    full_text += chunk.text
                    # On convertit le texte en Markdown au fur et à mesure
                    live.update(Panel(Markdown(full_text), border_style="blue", expand=False))
            
            console.print("\n") # Espace final
            
        except Exception as e:
            console.print(f"\n[bold red]❌ Erreur :[/bold red] {e}")

if __name__ == "__main__":
    main()