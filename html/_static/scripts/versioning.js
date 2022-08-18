(() => {
    fetch(`/gym-docs/_static/versions_menu.html`).then(response => {
        response.text().then(text => {
            const container = document.createElement("div");
            container.innerHTML = text;
            document.querySelector("body").appendChild(container);
            // innerHtml doenst evaluate scripts, we need to add them dynamically
            Array.from(container.querySelectorAll("script")).forEach(oldScript => {
                const newScript = document.createElement("script");
                Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
                newScript.appendChild(document.createTextNode(oldScript.innerHTML));
                oldScript.parentNode.replaceChild(newScript, oldScript);
            });
        });
    });
})()