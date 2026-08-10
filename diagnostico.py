"""
Descobre por que as transcrições pararam de funcionar.

Testa um vídeo só e mostra o erro real, em vez de escondê-lo.

Uso:
    python diagnostico.py
"""

import time

VIDEO_TESTE = "BQRT4Hi7nA8"   # Jutland — vídeo longo, do lote 02
IDIOMAS = ["en", "pt", "pt-BR"]

EXPLICACOES = {
    "RequestBlocked":
        "O YouTube está recusando requisições deste IP.\n"
        "   É o caso mais comum: acontece depois de muitos pedidos seguidos.\n"
        "   Costuma passar sozinho em algumas horas.",
    "IpBlocked":
        "O YouTube bloqueou este endereço de IP.\n"
        "   Mesma causa do anterior, versão mais dura.",
    "PoTokenRequired":
        "O YouTube passou a exigir um token de sessão para este vídeo.\n"
        "   Costuma ser resolvido usando os cookies de um navegador logado.",
    "TranscriptsDisabled":
        "Este vídeo específico tem legendas desativadas pelo canal.\n"
        "   Se só alguns vídeos falham, é isso — e não há o que fazer.",
    "NoTranscriptFound":
        "O vídeo tem legendas, mas não nos idiomas pedidos.\n"
        "   Ajuste a lista IDIOMAS no coletar.py.",
    "VideoUnavailable":
        "O vídeo não está mais disponível publicamente.",
    "AgeRestricted":
        "O vídeo tem restrição de idade e exige login.",
}

print("\n" + "=" * 62)
print("DIAGNÓSTICO DE TRANSCRIÇÕES")
print("=" * 62)

try:
    import youtube_transcript_api as pacote
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("\nA biblioteca não está instalada. Rode:")
    print("   pip install youtube-transcript-api\n")
    raise SystemExit

print(f"\nbiblioteca instalada: versão {getattr(pacote, '__version__', 'desconhecida')}")
print(f"vídeo de teste: {VIDEO_TESTE}")

api = YouTubeTranscriptApi()

print("\n1) Listando as legendas disponíveis…")
try:
    disponiveis = api.list(VIDEO_TESTE)
    for t in disponiveis:
        tipo = "automática" if t.is_generated else "manual"
        print(f"   - {t.language_code:8} ({tipo})")
except Exception as e:
    nome = type(e).__name__
    print(f"   FALHOU: {nome}")
    print(f"\n   >>> {EXPLICACOES.get(nome, 'Erro não catalogado. Mensagem completa abaixo.')}")
    print(f"\n   mensagem original:\n   {str(e)[:600]}")
    print("\n" + "=" * 62 + "\n")
    raise SystemExit

print("\n2) Baixando a transcrição…")
time.sleep(2)
try:
    dados = api.fetch(VIDEO_TESTE, languages=IDIOMAS)
    texto = " ".join(t.text for t in dados)
    print(f"   FUNCIONOU: {len(texto.split())} palavras")
    print(f"   início: {texto[:160]}…")
    print("\n   >>> As transcrições estão funcionando agora.")
    print("       Se o lote falhou antes, foi bloqueio temporário por excesso")
    print("       de pedidos. O coletar.py novo já espera entre um vídeo e outro.")
except Exception as e:
    nome = type(e).__name__
    print(f"   FALHOU: {nome}")
    print(f"\n   >>> {EXPLICACOES.get(nome, 'Erro não catalogado. Mensagem completa abaixo.')}")
    print(f"\n   mensagem original:\n   {str(e)[:600]}")

print("\n" + "=" * 62 + "\n")
