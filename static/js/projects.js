document.addEventListener('DOMContentLoaded', function() {
    const projectTabs = document.querySelectorAll('.project-tab');

    projectTabs.forEach(tab => {
        const row = tab.querySelector('.project-row');
        const content = tab.querySelector('.project-content');
        const icon = tab.querySelector('.expand-icon');
        
        row.addEventListener('click', function(e) {
            // Prevent any parent handlers from being executed
            e.stopPropagation();
            
            // Close all other tabs smoothly
            projectTabs.forEach(otherTab => {
                if (otherTab !== tab && otherTab.classList.contains('expanded')) {
                    const otherContent = otherTab.querySelector('.project-content');
                    otherTab.classList.remove('expanded');
                    otherContent.style.maxHeight = '0px';
                }
            });
            
            // Toggle current tab
            const isExpanding = !tab.classList.contains('expanded');
            tab.classList.toggle('expanded');
            
            // Set specific height for smooth animation
            if (isExpanding) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = '0px';
            }
        });
    });
});