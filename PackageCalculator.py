import math
class Package():
    def __init__(self, annualIncome):
        self.annualIncome = annualIncome
        print(f'税前年收入为{annualIncome}')
    
    def getCompanyBenefits(self, income):
         # 养老金
        pension = 0.2

        # 医疗保险
        health_care = 0.06

        # 失业保险
        umemployment = 0.02
        

        # 公积金：理论上和单位缴存比例一致
        house = 0.12

        benefits = income * (pension + health_care + umemployment + house)
        print(f'单位应缴纳的三险一金为{benefits}')

        return benefits
    
    def getPersonalBenefits(self, income):
        # 养老金
        pension = 0.08

        # 医疗保险
        health_care = 0.02

        # 失业保险
        umemployment = 0.005

        # 公积金：理论上和单位缴存比例一致
        house = 0.12

        benefits = income * (pension + health_care + umemployment + house)
        print(f'个人应缴纳的三险一金为{benefits}')

        return benefits
    
    def getTax(taxable_income, monthly_income=1):
    
        # 应纳税额 = 应纳税所得额 * 税率 - 速算扣除数
        
        table = [(5000, 0),
                 (8000, 0.03),
                 (17000, 0.1),
                 (30000, 0.2),
                 (40000, 0.25),
                 (60000, 0.30),
                 (85000, 0.35),
                 (math.inf,0.45),]  

        if monthly_income != 1:
            # 其他情况，默认是年度收入
            table = [(base * 12, rate) for base, rate in table ]

        tax = 0
        taxed_income = 0

        for i in range(len(table)):
            base, rate = table[i]

            if i < len(table):
                prevBase, prevRate = table[i-1]

                # 如果超过了当前的界限
                if taxable_income >= base:
                    tax += (base - taxed_income) * rate
                    taxed_income = base

                # 如果卡在两个界限之间
                elif taxable_income > prevBase:
                    tax += (taxable_income - taxed_income) * rate
                    taxed_income = taxable_income


        print(f'应税所得额{taxable_income}应纳税额为{tax}')

        return tax
    
    
    def getPackage(self):
        company_benefits = self.getCompanyBenefits(self.annualIncome)
        personalbenefits = self.getPersonalBenefits(self.annualIncome)
        
        
        taxable_income = self.annualIncome - personalbenefits
        tax = getTax(taxable_income, 0)
        
        package = self.annualIncome - tax + personalbenefits + company_benefits
        print(f'总的package是{package}')

        return package

Package(40000*12).getPackage()
