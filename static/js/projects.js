document.addEventListener('DOMContentLoaded', function() {
    const projectTabs = document.querySelectorAll('.project-tab');

    projectTabs.forEach(tab => {
        const row = tab.querySelector('.project-row');
        const content = tab.querySelector('.project-content');
        
        row.addEventListener('click', function() {
            // Close all other tabs
            projectTabs.forEach(otherTab => {
                if (otherTab !== tab && otherTab.classList.contains('expanded')) {
                    otherTab.classList.remove('expanded');
                    otherTab.querySelector('.project-content').style.maxHeight = null;
                }
            });
            
            // Toggle current tab
            tab.classList.toggle('expanded');
            
            // Animate content height
            if (tab.classList.contains('expanded')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = null;
            }
        });
    });
});