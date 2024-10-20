import './App.css';
import { React, useState, useEffect } from 'react';
import { TaskProvider } from './context';
import { TaskForm, TaskItems ,SearchTask} from './components';

const App = () => {
    const [tasks, setTasks] = useState([]);
    const [selectedTaskId, setSelectedTaskId] = useState(null);
    const [loading, setLoading] = useState(false); 
    const [error, setError] = useState(null); 
    const [searchedTask, setSearchedTask] = useState(null);

    // Fetch all tasks from backend on component mount
    useEffect(() => {
        fetchTasks();
    }, []);

    // Fetch tasks from backend
    const fetchTasks = async () => {
        setLoading(true);
        try {
            const response = await fetch("http://localhost:8001/api/tasks");
            if (!response.ok) throw new Error('Failed to fetch tasks');
            const data = await response.json();
            setTasks(data.map(task => ({
                id: task["id"],
                title: task["title"],
                description: task["description"],
                status: task["status"],
                createdAt: task["createdAt"],
                updatedAt: task["updatedAt"],
                deadline: task["deadline"],
                createdBy: task["createdBy"],
                updatedBy: task["updatedBy"],
               
            })));
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };


    // Add task to backend
    const addTask = async (task) => {
        console.log("inside add task");
        try {
            const response = await fetch("http://localhost:8001/api/tasks", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(task),
            });

            if (response.ok) {
                const newTask = await response.json();
                const task = {
                    id: newTask.id, 
                    title: newTask.title,
                    description: newTask.description,
                    status: newTask.status,
                    createdAt: newTask.createdAt,
                    updatedAt: newTask.updatedAt,
                    deadline: newTask.deadline,
                    createdBy: newTask.createdBy,
                    updatedBy: newTask.updatedBy,
                };
                setTasks((prev) => [{ ...task }, ...prev]); // Add the new task to local state
            }
        } catch (error) {
            console.error("Error adding task:", error);
        }
    };

        // Update task in backend
    const updateTask = async (taskid,task) => {
        console.log("inside update task", taskid);
        console.log(task);
        if (taskid ) {
            try {
                const response = await fetch(`http://localhost:8001/api/tasks/${taskid}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(task),
                });

                if (response.ok) {
                    const updatedTask = await response.json();
                    setTasks((prev) =>
                        prev.map((prevtask) => (prevtask.id === updatedTask.id ? updatedTask : prevtask))
                    ); 
                }
            } catch (error) {
                console.error("Error updating task:", error);
            }
        }
    };


    
    // Delete task from backend
    const deleteTask = async (taskid) => {
        if (taskid) {
            try {
                const response = await fetch(`http://localhost:8001/api/tasks/${taskid}`, {
                    method: "DELETE",
                });

                if (response.ok) {
                    
                    setTasks((prev) => prev.filter((task) => task.id !== taskid)); // Remove the task from local state
                    setSelectedTaskId(null); // Clear selected task ID after deletion
                }
            } catch (error) {
                console.error("Error deleting task:", error);
            }
        }
    };

    const searchTask = async (id) => {
        console.log("inside search task");
        console.log(id);
        try {
            const response = await fetch(`http://localhost:8001/api/tasks/${id}`); 
            
            if (!response.ok) {
                throw new Error(`Task not found with ID: ${id}`);
            }
    
            const data = await response.json();
          
            const task = {
                id: data.id, 
                title: data.title,
                description: data.description,
                status: data.status,
                createdAt: data.createdAt,
                updatedAt: data.updatedAt,
                deadline: data.deadline,
                createdBy: data.createdBy,
                updatedBy: data.updatedBy,
            };
    
            setTasks([task]);
            setSearchedTask(task);
            console.log("Searched Task:", task);
            console.log(searchedTask);
            return data;
    
        } catch (error) {
            console.error("Error searching task:", error);
        }
    };

  
    

    return (
        <TaskProvider value={{ tasks, addTask, updateTask, deleteTask, searchTask,searchedTask }}>
            <div className="bg-[#172842] min-h-screen py-8">
                <div className="w-full max-w-2xl mx-auto shadow-md rounded-lg px-4 py-3 text-white">
                    <h1 className="text-2xl font-bold text-center mb-8 mt-2">Manage Your Tasks</h1>
                    <div className="mb-4">
                        <SearchTask/> 
                        <TaskForm onSubmit={addTask}  selectedTaskId={selectedTaskId} />
                    </div>
                    {loading && <p className="text-center">Loading tasks...</p>}
                    {error && <p className="text-red-500 text-center">{error}</p>}
                    <div className="flex flex-wrap gap-y-3">
                        <ul>
                            {searchedTask !== null ? ( // Conditionally render the searched task
                                <li>
                                    <TaskItems task={searchedTask} /> {/* Display the searched task */}
                                </li>
                            ) : (
                                Array.isArray(tasks) && tasks.length > 0 ? (
                                    tasks.map((task) => (
                                        <li key={task.id}>
                                            <TaskItems task={task} />
                                        </li>
                                    ))
                                ) : (
                                    <li>No tasks available.</li>
                                )
                            )}
                        </ul>
                    </div>
                </div>
            </div>
        </TaskProvider>
    );


};

export default App;



