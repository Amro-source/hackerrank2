using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Solution
{
    public class EmployeesManagement
    {





    // List of employees
    private List<Employee> employees;

    // Constructor
    public EmployeesManagement(List<Employee> employees)
    {
        this.employees = employees;
    }

        public static Dictionary<string, int> AverageAgeForEachCompany(List<Employee> employees)
        {
                    // Group employees by company and select the average age for each group
        var result = employees.GroupBy(e => e.Company)
                              .Select(g => new { Company = g.Key, AverageAge = (int)Math.Round(g.Average(e => e.Age)) })
                              .OrderBy(r => r.Company)
                              .ToDictionary(r => r.Company, r => r.AverageAge);
        return result;
            
        }
        
        public static Dictionary<string, int> CountOfEmployeesForEachCompany(List<Employee> employees)
        {
                    // Group employees by company and select the count for each group
        var result = employees.GroupBy(e => e.Company)
                              .Select(g => new { Company = g.Key, Count = g.Count() })
                              .OrderBy(r => r.Company)
                              .ToDictionary(r => r.Company, r => r.Count);
        return result;
            
        }
        
        public static Dictionary<string, Employee> OldestAgeForEachCompany(List<Employee> employees)
        {
            
            // Group employees by company and select the employee with the maximum age for each group
        var result = employees.GroupBy(e => e.Company)
                              .Select(g => new { Company = g.Key, OldestEmployee = g.OrderByDescending(e => e.Age).First() })
                              .OrderBy(r => r.Company)
                              .ToDictionary(r => r.Company, r => r.OldestEmployee);
        return result;
        }

        public static void Main()
        {   
            int countOfEmployees = int.Parse(Console.ReadLine());
            
            var employees = new List<Employee>();
            
            for (int i = 0; i < countOfEmployees; i++)
            {
                string str = Console.ReadLine();
                string[] strArr = str.Split(' ');
                employees.Add(new Employee { 
                    FirstName = strArr[0], 
                    LastName = strArr[1], 
                    Company = strArr[2], 
                    Age = int.Parse(strArr[3]) 
                    });
            }
            
            foreach (var emp in AverageAgeForEachCompany(employees))
            {
                Console.WriteLine($"The average age for company {emp.Key} is {emp.Value}");
            }
            
            foreach (var emp in CountOfEmployeesForEachCompany(employees))
            {
                Console.WriteLine($"The count of employees for company {emp.Key} is {emp.Value}");
            }
            
            foreach (var emp in OldestAgeForEachCompany(employees))
            {
                Console.WriteLine($"The oldest employee of company {emp.Key} is {emp.Value.FirstName} {emp.Value.LastName} having age {emp.Value.Age}");
            }
        }
    }
    
    public class Employee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int Age { get; set; }
        public string Company { get; set; }
    }
}   
