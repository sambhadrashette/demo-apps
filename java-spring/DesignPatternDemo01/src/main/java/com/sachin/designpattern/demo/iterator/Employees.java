package com.sachin.designpattern.demo.iterator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Employees implements Iterable<Employee> {
    List<Employee> employees;

    public Employees() {
        employees = new ArrayList<>();
        employees.add(new Employee(1, "Sachin", 5));
        employees.add(new Employee(1, "Rahul", 7));
        employees.add(new Employee(2, "Sumit", 9));
    }

    @Override
    public Iterator iterator() {
        return employees.iterator();
    }
}
