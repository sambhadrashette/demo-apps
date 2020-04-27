package com.sachin.designpattern.demo.iterator;

public class EmployeeTester {
    public static void main(String[] args) {
        Employees employees = new Employees();
        for (Employee emp: employees) {
            System.out.println(emp);
        }
    }
}
