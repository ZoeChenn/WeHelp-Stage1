document.addEventListener('DOMContentLoaded', () => {
  const deleteBtns = document.querySelectorAll('#deleteBtn');
  // console.log("綁定完成")
  deleteBtns.forEach(button => {
    button.addEventListener('click', (e) => {
      // alert("有點到刪除按鈕");
      const contentId = button.getAttribute('contentId');
      // alert(contentId);
      const confirmDelete = confirm('確定要刪除此留言嗎？');
      e.preventDefault();
      if (confirmDelete) {
        let newPath = "/deleteMessage/" + contentId;
        window.location.href = newPath;
      }
    });
  });
});