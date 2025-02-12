# Twitter Clone

Um clone moderno do Twitter desenvolvido com Django, oferecendo uma experiência de usuário fluida e interativa com recursos em tempo real.

## 🚀 Funcionalidades

### Autenticação
- Sistema completo de autenticação de usuários
- Registro de nova conta 
- Login com username/email e senha
- Recuperação de senha 
- Logout seguro

### Feed e Tweets
- Feed interativo com atualizações em tempo real
- Criação de tweets com limite de 280 caracteres
- Contador de caracteres dinâmico
- Animações suaves ao postar novos tweets
- Carregamento automático de novos tweets

### Interações
- Sistema de likes em tweets
  - Animação de coração ao dar like
  - Contador de likes em tempo real
- Sistema de follow para outros usuários
  - Notificação visual ao seguir um usuário
  - Lista de "Who to follow" com sugestões

### Busca
- Barra de busca em tempo real
- Busca por conteúdo de tweets
- Resultados atualizados dinamicamente
- Interface responsiva para resultados

### Interface
- Design moderno e responsivo
- Tema consistente com o Twitter original
- Sidebars interativas
- Menu hamburguer para mobile
- Animações e transições suaves
- Trending Topics
- Notificações visuais para ações do usuário

### 🛠 Tecnologias Utilizadas
- **Frontend:**
  - **HTML5 & CSS3:** Uso de marcação semântica e estilizações modernas, com animações e transições suaves para uma experiência visual atraente.
  - **JavaScript (ES6+):** Manipulação dinâmica da interface e lógica interativa para melhor experiência de usuário.
  - **Bootstrap 5:** Framework responsivo que agiliza a criação de layouts consistentes em dispositivos móveis e desktop.
  - **HTMX:** Permite interações assíncronas, atualizando partes da página sem recarregar totalmente.
  - **Alpine.js:** Gerenciamento leve de estado e reatividade para componentes dinâmicos.

- **Backend:**
  - **Django:** Framework robusto que gerencia a lógica de negócios e a renderização de templates. Vale ressaltar que os Django Templates processam a interface no servidor, gerando HTML que é enviado para o cliente; assim, embora componham a camada visual, seu processamento ocorre no back-end.
  - **Django AllAuth:** Facilita a autenticação de usuários, incluindo integração com provedores sociais.
  - **Django REST Framework:** (Opcional) Para construção de APIs RESTful que suportam a comunicação com o frontend.
  - **PostgreSQL:** Banco de dados relacional escalável e seguro para armazenamento de informações.
  - **Gunicorn:** Servidor WSGI eficiente para a execução da aplicação em ambientes de produção.
  - **WhiteNoise:** Otimiza a entrega de arquivos estáticos, melhorando o desempenho em produção.

- **DevOps & Deployment:**
  - **Docker & Docker Compose:** Containerização que garante consistência entre ambientes de desenvolvimento e produção.
  - **Poetry:** Gerencia dependências e configura o ambiente Python de forma moderna e isolada.
  - **Railway:** Plataforma de deploy que simplifica a publicação e a escalabilidade da aplicação.

## 💻 Layout Responsivo
- Desktop: Layout completo com três colunas
- Mobile: 
  - Menu hamburguer para navegação
  - Interface adaptada para telas menores
  - Experiência otimizada para dispositivos móveis

## 🔧 Recursos Técnicos
- Atualizações em tempo real com HTMX
- Animações suaves com CSS
- Gerenciamento de estado com Alpine.js
- Sistema de autenticação seguro
- Proteção CSRF
- Validações de formulário
- Feedback visual para ações do usuário

## 🎨 Design
- Gradientes modernos
- Efeitos de glassmorphism
- Animações de hover e clique
- Ícones vetoriais
- Tipografia consistente
- Paleta de cores do Twitter

## 🔒 Segurança
- Autenticação segura
- Proteção contra CSRF
- Validação de dados
- Sanitização de input
- Sessões seguras

## 🌟 Diferenciais
- Interface moderna e responsiva
- Animações fluidas
- Atualizações em tempo real
- Código limpo e organizado
- Experiência de usuário otimizada
 
