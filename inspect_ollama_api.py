import inspect
import ollama
print('ok')
print('version', getattr(ollama, '__version__', 'unknown'))
print('has chat', hasattr(ollama, 'chat'))
print('has generate', hasattr(ollama, 'generate'))
print('attrs', [n for n in dir(ollama) if n in ('chat','generate','create','image','Model','vision')])
print('chat doc:', inspect.getdoc(ollama.chat)[:400] if hasattr(ollama, 'chat') and inspect.getdoc(ollama.chat) else 'no-doc')
print('generate doc:', inspect.getdoc(ollama.generate)[:400] if hasattr(ollama, 'generate') and inspect.getdoc(ollama.generate) else 'no-doc')
