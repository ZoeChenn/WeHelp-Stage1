document.addEventListener('DOMContentLoaded', () => {
  const deleteBtns = document.querySelectorAll('#deleteBtn');
  deleteBtns.forEach(button => {
    button.addEventListener('click', (e) => {
      const contentId = button.getAttribute('contentId');
      const confirmDelete = confirm('確定要刪除此留言嗎？');
      e.preventDefault();
      if (confirmDelete) {
        let newPath = "/deleteMessage/" + contentId;
        window.location.href = newPath;
      }
    });
  });
});

document.getElementById('searchUsername').addEventListener('click', ()=> {
  const searchUsername = document.querySelector('#searchUsernameInput').value;
    if (searchUsername) {
      fetch(`/api/member?username=${searchUsername}`)
        .then(response => response.json())
        .then(data => {
          console.log(data)
          const memberDataDiv = document.getElementById('memberData');
          const nameValue = data.data.name;
          memberDataDiv.innerHTML = `<p>${nameValue} (${data.data.username})</p>`
        })
        .catch(error => console.error('Error:', error));
  }
})

document.getElementById('updateName').addEventListener('click', () => {
  const newName = document.querySelector('#updateNameInput').value;
  if (newName) {
    fetch('/api/member', {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "name": newName })
    })
    .then(response => response.json())
    .then(data => {
      const updateResultDiv = document.getElementById('updateResult');
      if (data.ok) {
        updateResultDiv.textContent = '姓名已成功更新。';
        updateMemberName(newName);
      } else {
        updateResultDiv.textContent = '更新失敗，請確認您已登入。';
      }
    })
    .catch(error => console.error('Error:', error));
  }
});

function updateMemberName(name) {
  const updateMemberName = document.getElementById('newMemberName');
  if (updateMemberName) {
    updateMemberName.innerHTML = `<p id="newMemberName">${name}，歡迎登入系統</p>`;
  }
}