function updateJumpNav() {
   const jumpNav = document.querySelector(".alphabetical-index");
   const sectionContainers = document.querySelectorAll(".section-container")
   const firstSectionContainer = sectionContainers[0].getBoundingClientRect();
   const lastSectionContainer = sectionContainers[sectionContainers.length - 1].getBoundingClientRect();
   if(firstSectionContainer.top >= 40) jumpNav.style.top = (firstSectionContainer.top - 7) + "px";
   else if (lastSectionContainer.bottom <= window.innerHeight - 85) jumpNav.style.top = `${lastSectionContainer.bottom - jumpNav.offsetHeight}px`;
   else jumpNav.style.top = "33px";
}
document.addEventListener("DOMContentLoaded", updateJumpNav);
document.addEventListener("scroll", updateJumpNav);
function updateJumpNavHighlight() {
   const sections = document.querySelectorAll(".section-container");
   const navLinks = document.querySelectorAll(".alphabetical-index a");
   let activeSectionId = null;
   sections.forEach(section => {
      const rect = section.getBoundingClientRect();
      if (rect.top < window.innerHeight/2) activeSectionId = section.id;
   });
   navLinks.forEach(link => link.classList.remove("active"));
   if (activeSectionId) {
      const activeLink = document.querySelector(`.alphabetical-index a[href="#${activeSectionId}"]`);
      if (activeLink) activeLink.classList.add("active");
   }
}

document.addEventListener("DOMContentLoaded", updateJumpNavHighlight);
document.addEventListener("scroll", updateJumpNavHighlight);
