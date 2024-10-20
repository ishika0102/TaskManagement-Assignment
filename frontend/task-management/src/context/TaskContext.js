import { createContext, useContext } from "react";

export const TaskContext = createContext({
        tasks: [
                {
                        id: 1,
                        title: "Task 1",
                        description: "Description for Task 1",
                        deadline: "2022-01-01",
                        createdBy: "user1",
                        updatedBy: "user1",}
        ],
        searchedTask: {
                id: 1,
                title: "Task 1",
                description: "Description for Task 1",
                deadline: "2022-01-01",
                createdBy: "user1",
                updatedBy: "user1",
        },
        addTask : (task) => {},
        updateTask : (id,task) => {},
        deleteTask : (id) => {},
        toggleCompleted : (id) => {},
        searchTask : (id) => {},
});

export const useTask = () => {
        return useContext(TaskContext)
}

export const TaskProvider = TaskContext.Provider

