#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const tasksCompleted = {};
    todos.forEach((todo) => {
      if (todo.tasksCompleted && tasksCompleted[todo.userId] === undefined) {
        tasksCompleted[todo.userId] = 1;
      } else if (todo.tasksCompleted) {
        tasksCompleted[todo.userId] += 1;
      }
    });
    console.log(tasksCompleted);
  }
});
