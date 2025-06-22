(function main() {
  const extractUsers = () => {
    const users = Array.from(document.querySelectorAll("div[role='dialog'] li"))
      .map(el => {
        const userEl = el.querySelector("span a");
        return userEl ? userEl.textContent.trim() : null;
      })
      .filter(Boolean);
    return users;
  };

  const download = (filename, text) => {
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  const users = extractUsers();
  const csv = users.join("\n");
  download("followers.csv", csv);
})();

