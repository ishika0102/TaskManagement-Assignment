

// SearchTask.js
import React, { useState, useContext } from 'react';
import { TaskContext } from "../context/TaskContext";
const SearchTask = () => {
    const [taskId, setTaskId] = useState('');
    const [taskData, setTaskData] = useState([]); 

    const { searchTask } = useContext(TaskContext); // Import the searchTask function from TaskContext

    const handleSearch = async() => {
        if (taskId) {
            const task = await searchTask(taskId);
            console.log("inside search task");
            console.log(task);
        setTaskData(task); 
       
        setTaskData(task ? [task] : []);// Update state with the fetched task data
            setTaskId(''); // Clear input after search
        } else {
            alert("Please enter a task ID.");
        }
    };

    return (
        <>
        <div className="flex justify-center mb-4">
            <input
                type="text"
                placeholder="Enter Task ID"
                value={taskId}
                onChange={(e) => setTaskId(e.target.value)}
                className="border rounded px-2 py-1 mr-2 text-black"
                />
            <button onClick={handleSearch} className="bg-blue-500 text-white rounded px-3 py-1">
                Search Task

            </button>
        </div>
        </>
    );
};

export default SearchTask;

