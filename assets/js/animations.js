document.addEventListener('DOMContentLoaded', () => {
    // Register ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // Reveal Up
    gsap.utils.toArray('.reveal-up').forEach((elem) => {
        gsap.fromTo(elem, 
            { opacity: 0, y: 30 },
            { 
                opacity: 1, 
                y: 0, 
                duration: 1, 
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: elem,
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                }
            }
        );
    });

    // Reveal Left
    gsap.utils.toArray('.reveal-left').forEach((elem) => {
        gsap.fromTo(elem, 
            { opacity: 0, x: -50 },
            { 
                opacity: 1, 
                x: 0, 
                duration: 1.2, 
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: elem,
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                }
            }
        );
    });

    // Reveal Right
    gsap.utils.toArray('.reveal-right').forEach((elem) => {
        gsap.fromTo(elem, 
            { opacity: 0, x: 50 },
            { 
                opacity: 1, 
                x: 0, 
                duration: 1.2, 
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: elem,
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                }
            }
        );
    });

    // Stagger Cards
    gsap.from('.stagger-card', {
        opacity: 0,
        y: 20,
        stagger: 0.2,
        duration: 0.8,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.stagger-container',
            start: 'top 80%'
        }
    });
});
