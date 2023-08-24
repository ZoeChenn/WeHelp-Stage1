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

function updateMemberName(name) {
  const updateMemberName = document.getElementById('newMemberName');
  if (updateMemberName) {
    updateMemberName.textContent = `${name}，歡迎登入系統`;
  }
}

document.getElementById('searchUsername').addEventListener('click', () => {
  const searchUsernameInput = document.getElementById('searchUsernameInput');
  const isValid = searchUsernameInput.checkValidity();
  if (!isValid) {
    const memberData = document.getElementById('memberData');
    memberData.textContent = searchUsernameInput.validationMessage;
    return;
  }
  const searchUsername = document.querySelector('#searchUsernameInput').value;
    if (searchUsername) {
      fetch(`/api/member?username=${searchUsername}`)
        .then(response => response.json())
        .then(data => {
          console.log(data)
          const nameValue = data.data.name;
          memberData.innerHTML = `<p>${nameValue} (${data.data.username})</p>`
        })
        .catch(error => console.error('Error:', error));
  }
});

document.getElementById('updateName').addEventListener('click', () => {
  const updateNameInput = document.getElementById('updateNameInput');
  const isValid = updateNameInput.checkValidity();
  const updateResult = document.getElementById('updateResult');
  if (!isValid) {
    updateResult.textContent = updateNameInput.validationMessage;
    return;
  }
  updateResult.textContent = '';
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
      if (data.ok) {
        updateResult.textContent = '姓名已成功更新。';
        updateMemberName(newName);
      } else {
        updateResult.textContent = '更新失敗，請確認您已登入。';
      }
    })
    .catch(error => console.error('Error:', error));
  }
});