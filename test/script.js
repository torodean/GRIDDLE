const links = document.querySelectorAll('.navbar a');
const iframe = document.getElementById('contentFrame');

links.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        // Remove active class from all links
        links.forEach(l => l.classList.remove('active'));
        // Add active class to clicked link
        link.classList.add('active');
        // Load the selected page in the iframe
        iframe.src = link.dataset.url;
    });
});

document.querySelectorAll('.tree .folder').forEach(folder => {
  folder.addEventListener('click', () => {
    folder.parentElement.classList.toggle('expanded');
  });
});

document.querySelectorAll('[data-url]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const url = link.getAttribute('data-url');
    document.getElementById('contentFrame').src = url;
  });
});
