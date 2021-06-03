<template>
  <div class="TodoController">
    <div class="TodoController-Select">
      <label for="order">Order</label>
      <select name="order" id="order" class="TodoController-Select-Box">
        <option value="date-asc">Date Asc</option>
        <option value="date-desc">Date Desc</option>
        <option value="name-asc">Name Asc</option>
        <option value="name-desc">Name Desc</option>
      </select>
    </div>
    <button class="TodoController-ClearAllBtn">Delete All</button>
  </div>
</template>