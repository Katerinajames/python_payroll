class Employee:
	
 def __init__(self,first, last,  ssn ):
  self.first=first
  self.last=last
  self.ssn=ssn

  def earnings(self):	    	   
   raise NotImplementedError, "Cannot call abstract method"
print"--------------------------------------------"

class SalariedEmployee(Employee):
   def __init__(self,first, last,  ssn,salary ):
          Employee.__init__(self,first, last,  ssn)
          self.setsalary(salary)


   def setsalary(self,salary):
        if (salary>=0):
               self.salary=salary       
        else:      
           raise ValueError,"Invalid  value"       

   def  earnings(self):
        return self.salary
        
        
        
   
        
print"--------------------------------------------"

class HourlyEmployee(Employee):
  def __init__(self,first, last,  ssn ,hourlywage,hoursworked):
        Employee.__init__(self,first, last,  ssn)
        self.sethourlywage(hourlywage)
        self.sethoursworkred(hoursworked)
      
      
  def sethourlywage  (self,hourlywage):
        if    (hourlywage>0):
             self.hourlywage=hourlywage 
        else:
             raise  ValueError,"To poso prepei na einai megalitero apo 0.0" 
  
  def gethourlywage(self):
      return self.hourlywage    
    
  def sethoursworkred(self,hoursworked):
       if      ((hoursworked >= 0.0 ) and ( hoursworked <= 168.0 ) ):
              self.hoursworked=hoursworked
       else:
            raise ValueError,"To poso prepei na einai megalitero apo 0.0" 	  
 
  def gethoursworked(self):
         return self.hoursworked
 
  def earnings(self):
       if (self.gethoursworked()<=40): 
           return self.gethourlywage()*self.gethoursworked()
       else:
           return 40 *self.gethourlywage()+( self.gethoursworked() - 40 ) * self.gethourlywage() * 1.5

      
      


  
print"--------------------------------------------"     
       
class CommissionEmployee(Employee):
        def __init__(self,first, last,  ssn,grossales,commissionrate):	
             Employee.__init__(self,first, last,  ssn)	
             self.setgrossales(grossales)
             self.setcommissionrate(commissionrate)
        def setcommissionrate(self,commissionrate):
             if (commissionrate > 0.0 and  commissionrate < 1.0):
                    self.commissionrate = commissionrate
             else:
                  raise ValueError,"To poso prepei na einai megalitero apo 0.0" 
             
        def getcommissionrate(self):
 
             return  self.commissionrate 
     
        def  setgrossales(self,grossales):
             if ( grossales >= 0.0 ):
                self.grossales = grossales
             else:
              raise ValueError,"To poso prepei na einai megalitero apo 0.0" 
     
        def getgrossales(self):
              return   self.grossales  
    
        def earnings(self):
           return self.getgrossales()*self.getcommissionrate()
       



print"---------------------------------------------------------"

class BasePlusCommissionEmployee(CommissionEmployee):
   def __init__(self,first, last,  ssn,grossales,commissionrate,basesalary):
          CommissionEmployee.__init__(self,first, last,  ssn,grossales,commissionrate)
          self.setbasesalary(basesalary)   

   def setbasesalary(self,basesalary):
        if   basesalary>=0.0: 
            self.basesalary =basesalary;
        else:
         raise ValueError,"To poso prepei na einai megalitero apo 0.0" 
   def getbasesalary(self):
         return self.basesalary     
        
   def earnings(self):
       return self.getbasesalary() +self.getgrossales()*self.getcommissionrate()
        
        
print"---------------------------------------------------------"       
             
e=SalariedEmployee( "John", "Smith", "111-11-1111", 800.00 )     


c=CommissionEmployee("Sue", "Jones", "333-33-3333", 10000, 0.6 )

b=BasePlusCommissionEmployee("Bob", "Lewis", "444-44-4444", 5000, 0.4, 300 )
 

print  "Salaried Employee"

print  e.earnings()

h=HourlyEmployee( "Karen", "Price", "222-22-2222", 16.75, 40 )

print  "Hourly Employee"

print h.earnings()

print "Commision Employee"

print c.earnings()

print "Base Plus Commission Employee"


print b.earnings()

print "Table elements"


table=e,h,b

for i in table :
  print i.earnings()
 







