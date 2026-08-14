document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.querySelector(".oidc-login__toggle");
    const localLogin = document.querySelector(".oidc-login__local");
    const localSubmit = document.querySelector(".oidc-login__local-submit");

    if (!toggle || !localLogin || !localSubmit) {
        return;
    }

    toggle.addEventListener("click", () => {

        const isOpen = toggle.getAttribute("aria-expanded") === "true";

        toggle.setAttribute("aria-expanded", String(!isOpen));
        localLogin.classList.toggle("is-open", !isOpen);
        localSubmit.classList.toggle("is-open", !isOpen);

    });

});
