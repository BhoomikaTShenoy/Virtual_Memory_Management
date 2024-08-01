import tkinter as tk
from tkinter import messagebox
import time

class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulation")
        
        self.frame = tk.Frame(root)
        self.frame.pack(padx=50, pady=80)
        
        self.memory_size_label = tk.Label(self.frame, text="Memory Size:")
        self.memory_size_label.pack()
        self.memory_size_entry = tk.Entry(self.frame)
        self.memory_size_entry.pack()
        
        self.virtual_size_label = tk.Label(self.frame, text="Virtual Memory Size:")
        self.virtual_size_label.pack()
        self.virtual_size_entry = tk.Entry(self.frame)
        self.virtual_size_entry.pack()
        
        self.page_requests_label = tk.Label(self.frame, text="Page Requests:")
        self.page_requests_label.pack()
        self.page_requests_entry = tk.Entry(self.frame)
        self.page_requests_entry.pack()
        


        
        self.simulate_button = tk.Button(self.frame, text="Simulate", command=self.simulate)
        self.simulate_button.pack()

        self.results_text = tk.Text(self.frame, height=400, width=50)
        self.results_text.pack()

    def simulate(self):
        try:
    
            memory_size = int(self.memory_size_entry.get())
            virtual_size = int(self.virtual_size_entry.get())
            page_requests = list(map(int, self.page_requests_entry.get().split()))
            memory = []
            page = []
            page_faults = 0
            page_hit =0
            hit_ratio =0
            fault_ratio =0
            
            total_time=0
            start_time = time.time()
            time.sleep(2)
            end_time = time.time()
            total_time = end_time - start_time
        

            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Simulation Results:\n\n")
            self.results_text.insert(tk.END, "fifo:\n\n")
            
            for idx, request in enumerate(page_requests, start=1):
                if request not in memory:
                    page_faults += 1
                    if len(memory) < memory_size:
                        memory.append(request)
                    else:
                        removed_page = memory.pop(0)
                        memory.append(request)
                        result_text = f"Page {removed_page} replaced by Page {request}\n"
                        self.results_text.insert(tk.END, result_text)
                else:
                    page_hit+=1

            

                result_text = f"Process {idx}:\n"
                print("virtual memory maps from disk to main memory")
                result_text += f"Page Request: {request}\n"
                result_text += f"Memory State: {memory}\n"
                result_text += f"Page Faults: {page_faults}\n"
                result_text += f"Page Hit: {page_hit}\n"
                hit_ratio = (page_hit/(page_hit + page_faults))*100
                fault_ratio=(page_faults/(page_hit + page_faults))*100
                result_text += f"Hit Ratio: {hit_ratio}%\n"
                result_text += f"Fault Ratio: {fault_ratio}%\n"
                result_text += f"time taken: {total_time:.4f}\n\n"
                self.results_text.insert(tk.END, result_text)
            
            self.results_text.insert(tk.END, "optimal:\n\n")
            
            page_faults=0
            page_hit=0
            for idx, request in enumerate(page_requests, start=1):
                
                if request not in memory:
                    page_faults+=1
                    if len(memory) < 3:
                        memory.append(request)
                        
                    else:
                        removed_page = memory.pop()
                        memory.append(request)
                        result_text = f"Page {removed_page} replaced by Page {request}\n"
                        self.results_text.insert(tk.END, result_text)
                else:
                    page_hit+=1
                    
                    
                    
                result_text = f"Process {idx}:\n"
                result_text += f"Page Request: {request}\n"
                result_text += f"Memory State: {memory}\n"
                result_text += f"Page Faults: {page_faults}\n"
                result_text += f"Page Hit: {page_hit}\n"
                hit_ratio = (page_hit/(page_hit + page_faults))*100
                fault_ratio=(page_faults/(page_hit + page_faults))*100
                result_text += f"Hit Ratio: {hit_ratio}%\n"
                result_text += f"Fault Ratio: {fault_ratio}%\n"
                result_text += f"time taken: {total_time:.4f}\n\n"
                self.results_text.insert(tk.END, result_text)
                 

            self.results_text.insert(tk.END, "Simulation complete!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementGUI(root)
    root.mainloop()
