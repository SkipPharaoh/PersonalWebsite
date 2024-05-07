export function postScreenData(): void {
  const screenWidth = window.screen.width;
  const screenHeight = window.screen.height;
  const pixelRatio = window.devicePixelRatio;

  fetch("/api/update-views", {
    method: "POST",
    body: JSON.stringify({
      screenHeight,
      screenWidth,
      pixelRatio,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
