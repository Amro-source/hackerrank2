using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Solution {

    public class Team {
        
        
          // A member variable teamName [string]
    public string teamName;

    // A member variable noOfPlayers [integer]
    public int noOfPlayers;

    // A constructor function that takes 2 parameters and assigns them to teamName and noOfPlayers respectively
    public Team(string name, int players)
    {
        teamName = name;
        noOfPlayers = players;
    }

    // A member function AddPlayer(count) that takes an integer count as a parameter and increases noOfPlayers by count
    public void AddPlayer(int count)
    {
        noOfPlayers += count;
    }

    // A member function RemovePlayer(count) that takes an integer count as a parameter and tries to decrease noOfPlayers by count
    public void RemovePlayer(int count)
    {
        // If decreasing makes noOfPlayers negative, set it to zero instead
        if (noOfPlayers - count < 0)
        {
            noOfPlayers = 0;
        }
        else
        {
            noOfPlayers -= count;
        }
    }
        
        
        
        
        
        
        
        
    }

    public class Subteam: Team {
          // A constructor function that takes 2 parameters, teamName and noOfPlayers, and calls the base class constructor with these parameters
    public Subteam(string name, int players) : base(name, players)
    {
        // No need to write any code here as the base constructor does the work
    }

    // A member function ChangeTeamName(name) that takes a string name as a parameter and changes teamName to name
    public void ChangeTeamName(string name)
    {
        teamName = name;
    }
        
        
        
    }
    class Solution {
         static void Main(string[] args) {

            if (!typeof(Subteam).IsSubclassOf(typeof(Team))) {
                throw new Exception("Subteam class should inherit from Team class");
            }
            
            String str = Console.ReadLine();
            String[] strArr = str.Split();
            string initialName = strArr[0];
            int count = Convert.ToInt32(strArr[1]);
            Subteam teamObj = new Subteam(initialName, count);
            Console.WriteLine("Team " + teamObj.teamName + " created");
            
            str = Console.ReadLine();
            count = Convert.ToInt32(str);
            Console.WriteLine("Current number of players in team " + teamObj.teamName + " is " + teamObj.noOfPlayers);
            teamObj.AddPlayer(count);
            Console.WriteLine("New number of players in team " + teamObj.teamName + " is " + teamObj.noOfPlayers);
            
            
            str = Console.ReadLine();
            count = Convert.ToInt32(str);
            Console.WriteLine("Current number of players in team " + teamObj.teamName + " is " + teamObj.noOfPlayers);
            var res = teamObj.RemovePlayer(count);
            if (res) {
                Console.WriteLine("New number of players in team " + teamObj.teamName + " is " + teamObj.noOfPlayers);
            } else {
                Console.WriteLine("Number of players in team " + teamObj.teamName + " remains same");
            }
            
            str = Console.ReadLine();
            teamObj.ChangeTeamName(str);
            Console.WriteLine("Team name of team " + initialName + " changed to " + teamObj.teamName);
        }
    }
}
