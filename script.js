'use strict';

// Helper toggle function
const elementToggleFunc = function (elem) { 
    if (elem) elem.classList.toggle("active"); 
};

// Sidebar Toggle (Mobile / Tablet)
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

if (sidebar && sidebarBtn) {
    sidebarBtn.addEventListener("click", function () { 
        elementToggleFunc(sidebar); 
    });
}


// Filter Select (Mobile Dropdown)
const select = document.querySelector('[data-select]');
const selectItems = document.querySelectorAll('[data-select-item]');
const selectValue = document.querySelector('[data-select-value]');
const filterBtn = document.querySelectorAll('[data-filter-btn]');
const filterItems = document.querySelectorAll('[data-filter-item]');

if (select) {
    select.addEventListener('click', function () { 
        elementToggleFunc(this); 
    });
}

const filterFunc = function (selectedValue) {
    const target = selectedValue.trim().toLowerCase();
    for (let i = 0; i < filterItems.length; i++) {
        const itemCategory = (filterItems[i].dataset.category || '').trim().toLowerCase();
        if (target === "all" || target === itemCategory) {
            filterItems[i].classList.add('active');
        } else {
            filterItems[i].classList.remove('active');
        }
    }
};

for (let i = 0; i < selectItems.length; i++) {
    selectItems[i].addEventListener('click', function () {
        const selectedValue = this.innerText;
        if (selectValue) selectValue.innerText = selectedValue;
        if (select) elementToggleFunc(select);
        filterFunc(selectedValue);

        // Synchronize desktop buttons state
        for (let j = 0; j < filterBtn.length; j++) {
            if (filterBtn[j].innerText.trim().toLowerCase() === selectedValue.trim().toLowerCase()) {
                filterBtn.forEach(btn => btn.classList.remove('active'));
                filterBtn[j].classList.add('active');
                lastClickedBtn = filterBtn[j];
            }
        }
    });
}

// Filter Buttons (Desktop & Larger Screens)
let lastClickedBtn = filterBtn[0];

for (let i = 0; i < filterBtn.length; i++) {
    filterBtn[i].addEventListener('click', function () {
        const selectedValue = this.innerText;
        if (selectValue) selectValue.innerText = selectedValue;
        filterFunc(selectedValue);

        if (lastClickedBtn) lastClickedBtn.classList.remove('active');
        this.classList.add('active');
        lastClickedBtn = this;
    });
}

// Contact Form Validation
const form = document.querySelector('[data-form]');
const formInputs = document.querySelectorAll('[data-form-input]');
const formBtn = document.querySelector('[data-form-btn]');

if (form && formBtn) {
    for (let i = 0; i < formInputs.length; i++) {
        formInputs[i].addEventListener('input', function () {
            if (form.checkValidity()) {
                formBtn.removeAttribute('disabled');
            } else { 
                formBtn.setAttribute('disabled', '');
            }
        });
    }
}

// Page Navigation (Tabs: About, Resume, Portfolio, Blog, Contact)
const navigationLinks = document.querySelectorAll('[data-nav-link]');
const pages = document.querySelectorAll('[data-page]');

for (let i = 0; i < navigationLinks.length; i++) {
    navigationLinks[i].addEventListener('click', function () {
        const targetPage = this.innerHTML.trim().toLowerCase();

        for (let j = 0; j < pages.length; j++) {
            const pageName = (pages[j].dataset.page || '').trim().toLowerCase();
            if (targetPage === pageName) {
                pages[j].classList.add('active');
                navigationLinks[j].classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                pages[j].classList.remove('active');
                if (navigationLinks[j]) {
                    navigationLinks[j].classList.remove('active');
                }
            }
        }
    });
}

// Hash-based page navigation (e.g. #projects or #resume)
window.addEventListener('DOMContentLoaded', () => {
    const hash = (window.location.hash || '').replace('#', '').trim().toLowerCase();
    if (hash) {
        navigationLinks.forEach(link => {
            if (link.innerText.trim().toLowerCase() === hash) {
                link.click();
            }
        });
    }
});
