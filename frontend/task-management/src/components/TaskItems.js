import React, { useState } from 'react';
import { useTask } from '../context/TaskContext';

function TaskItems({ task }) {
    const { updateTask, deleteTask } = useTask();

    // Local state for all editable fields
    const [isEditable, setIsEditable] = useState(false);
    
    const [taskDetails, setTaskDetails] = useState({
        title: task.title,
        description: task.description,
        status: task.status,
        deadline: isNaN(new Date(task.deadline).getTime()) ? "" : new Date(task.deadline).toISOString().split('T')[0],
    });

    const handleEditToggleAndSave = () => {
        console.log("inside handleEditToggleAndSave",isEditable)
       
        
            const updatedTask = {
                ...task,
                ...taskDetails,
            };
            updateTask(task.id, updatedTask); 
        
        setIsEditable(!isEditable); 
    };


    return (
        <div className={`flex flex-col border border-black/10 rounded-lg p-4 gap-y-2 shadow-sm duration-300 text-black ${task.completed ? "bg-[#c6e9a7]" : "bg-[#ccbed7]"} w-80 h-auto`}>
          <div className="flex flex-col">
            <div className="flex justify-between items-center">
                <label className="font-semibold">Task ID:</label>
            </div>
            <p className="font-medium">{task.id}</p>
        </div>
            
            
            <div className="flex items-center">
            <div className="flex justify-between items-center">
                    <label className="font-semibold">Title:</label>
                </div>
                
                {isEditable ? (
                    <input
                        type="text"
                        value={taskDetails.title}
                        onChange={(e) => setTaskDetails({ ...taskDetails, title: e.target.value })}
                        className="ml-2 font-bold text-lg border outline-none bg-transparent w-full border-black/10 px-2 rounded"
                    />
                ) : (
                    <h3 className="ml-2 font-bold text-lg">{taskDetails.title}</h3>
                )}
            </div>

            <div className="flex flex-col">
                <div className="flex justify-between items-center">
                    <label className="font-semibold">Description:</label>
                </div>
                {isEditable ? (
                    <input
                        type="text"
                        value={taskDetails.description}
                        onChange={(e) => setTaskDetails({ ...taskDetails, description: e.target.value })}
                        className="border outline-none w-full bg-transparent rounded-lg border-black/10 px-2"
                    />
                ) : (
                    <p>{taskDetails.description}</p>
                )}
            </div>

            <div className="flex flex-col">
                <div className="flex justify-between items-center">
                    <label className="font-semibold">Status:</label>
                </div>
                {isEditable ? (
                    <input
                        type="text"
                        value={taskDetails.status}
                        onChange={(e) => setTaskDetails({ ...taskDetails, status: e.target.value })}
                        className="border outline-none w-full bg-transparent rounded-lg border-black/10 px-2"
                    />
                ) : (
                    <p>{taskDetails.status}</p>
                )}
            </div>

            <div className="flex flex-col">
                <div className="flex justify-between items-center">
                    <label className="font-semibold">Due Date:</label>
                </div>
                {isEditable ? (
                    <input
                        type="date"
                        value={taskDetails.deadline}
                        onChange={(e) => setTaskDetails({ ...taskDetails, deadline: e.target.value })}
                        className="border outline-none w-full bg-transparent rounded-lg border-black/10 px-2"
                    />
                ) : (
                    <p>{new Date(task.deadline).toLocaleDateString()}</p>
                )}
            </div>

            <div className="flex justify-between mt-2">
                <button
                    className='inline-flex w-8 h-8 rounded-lg text-sm border border-black/10 justify-center items-center bg-gray-50 hover:bg-gray-100 shrink-0'
                    onClick={handleEditToggleAndSave}
                >
                    {isEditable ? "💾" : "✏️"} {/* Save icon when in edit mode */}
                </button>
                <button
                    className='inline-flex w-8 h-8 rounded-lg text-sm border border-black/10 justify-center items-center bg-gray-50 hover:bg-gray-100 shrink-0'
                    onClick={() => deleteTask(task.id)}
                >
                    ❌
                </button>
            </div>
        </div>
    );
}

export default TaskItems;



