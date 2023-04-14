using System;
using System.Collections.Generic;
using System.IO;

namespace Solution
{

    public class NotesStore
    {
        public NotesStore() {
            
             notes = new Dictionary<string, List<string>>();
        notes.Add("completed", new List<string>());
        notes.Add("active", new List<string>());
        notes.Add("others", new List<string>());
            
        }
       // public void AddNote(String state, String name) {}
        //public List<String> GetNotes(String state) {}
        
      
    // A private dictionary to store the notes by state
    private Dictionary<string, List<string>> notes;


    // A method to add a note with the given name and state
    public void AddNote(string state, string name)
    {
        // If the name is empty, throw an exception
        if (name == "")
        {
            throw new Exception("Name cannot be empty");
        }

        // If the state is not valid, throw an exception
        if (!notes.ContainsKey(state))
        {
            throw new Exception($"Invalid state {state}");
        }

        // Otherwise, add the name to the corresponding list in the dictionary
        notes[state].Add(name);
    }

    // A method to get a list of note names with the given state
    public List<string> GetNotes(string state)
    {
        // If the state is not valid, throw an exception
        if (!notes.ContainsKey(state))
        {
            throw new Exception($"Invalid state {state}");
        }

        // Otherwise, return the corresponding list in the dictionary
        return notes[state];
    }
        
        
    } 

    public class Solution
    {
        public static void Main() 
        {
            var notesStoreObj = new NotesStore();
            var n = int.Parse(Console.ReadLine());
            for (var i = 0; i < n; i++) {
                var operationInfo = Console.ReadLine().Split(' ');
                try
                {
                    if (operationInfo[0] == "AddNote")
                        notesStoreObj.AddNote(operationInfo[1], operationInfo.Length == 2 ? "" : operationInfo[2]);
                    else if (operationInfo[0] == "GetNotes")
                    {
                        var result = notesStoreObj.GetNotes(operationInfo[1]);
                        if (result.Count == 0)
                            Console.WriteLine("No Notes");
                        else
                            Console.WriteLine(string.Join(",", result));
                    } else {
                        Console.WriteLine("Invalid Parameter");
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine("Error: " + e.Message);
                }
            }
        }
    }
}
