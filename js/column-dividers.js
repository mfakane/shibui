// Only explicit two-column groups get a separator. Both children keep their
// natural height; the absolute pseudo-element never affects their layout.
for (const group of document.querySelectorAll("[data-column-divider]")) {
  const [first, second] = group.children;
  if (!first || !second) continue;

  function updateDivider() {
    const host = group.getBoundingClientRect();
    const a = first.getBoundingClientRect();
    const b = second.getBoundingClientRect();
    const top = Math.max(a.top, b.top);
    const bottom = Math.min(a.bottom, b.bottom);
    const sideBySide = a.right <= b.left || b.right <= a.left;
    const gapMiddle =
      a.left < b.left ? (a.right + b.left) / 2 : (b.right + a.left) / 2;

    group.style.setProperty("--column-divider-x", `${gapMiddle - host.left}px`);
    group.style.setProperty("--column-divider-top", `${top - host.top}px`);
    group.style.setProperty(
      "--column-divider-height",
      `${sideBySide ? Math.max(0, bottom - top) : 0}px`,
    );
  }

  const observer = new ResizeObserver(updateDivider);
  observer.observe(group);
  observer.observe(first);
  observer.observe(second);
  updateDivider();
}
