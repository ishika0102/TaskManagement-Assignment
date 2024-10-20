import { React, useState } from 'react';
import { useTask } from "../context/TaskContext";

function TaskForm() {
    const [task, setTask] = useState({
        title: "",
        description: "",
        deadline: "",
        createdBy: ""
    });

    const { addTask } = useTask();

    const add = (e) => {
        console.log("inside add");
        e.preventDefault();
        if (!task) return;
        addTask(task);
        
        // Reset task state
        setTask({ title: "", description: "", deadline: "", createdBy: "" });
    }


    return (
        <form onSubmit={add} className='flex flex-col gap-4'>
            <input
                type="text"
                name="title"
                placeholder="Title"
                value={task.title}
                onChange={(e) => setTask({ ...task, title: e.target.value })}
                required
                style={{ color: 'black' }} 
            />
            <input
                type="text"
                name="description"
                placeholder="Description"
                value={task.description}
                onChange={(e) => setTask({ ...task, description: e.target.value })}
                required
                style={{ color: 'black' }} 
            />
            <input
                type="datetime-local" 
                name="deadline"
                value={task.deadline}
                onChange={(e) => setTask({ ...task, deadline: e.target.value })}
                required
                style={{ color: 'black' }} 
            />
            <input
                type="text"
                name="createdBy"
                placeholder="Created By"
                value={task.createdBy}
                onChange={(e) => setTask({ ...task, createdBy: e.target.value })}
                required
                style={{ color: 'black' }}
            />
            <button type="submit"
                className="bg-blue-600 text-white rounded px-4 py-1"
                >Add</button>
        </form>
    );
}

export default TaskForm;



