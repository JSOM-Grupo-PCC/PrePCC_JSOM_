// Função para manipular as mudanças no DOM
function handleMutations(mutationsList, observer) {
    mutationsList.forEach(mutation => {
        // Verifica se a classe "bg-white" foi adicionada a algum elemento
        if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
            const asideElement = document.getElementsByTagName("aside")[0];
            // Verifica se a classe "bg-white" está presente no elemento <aside>
            if (asideElement && asideElement.classList.contains('bg-white')) {
                // Remove a classe "bg-white" do elemento <aside>
                asideElement.classList.remove('bg-white');
            }
        }
    });
}

// Cria uma instância de MutationObserver com a função de manipulação de mutações
const observer = new MutationObserver(handleMutations);

// Configurações do MutationObserver
const config = { attributes: true, childList: true, subtree: true };

// Observa mudanças no DOM
observer.observe(document.body, config);
