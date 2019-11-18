class miles_class:
    def __init__(self, name):
        self.name = name
        #example name: "Region I Totals", "Vermont"

     def t_data(self, mileage):
            self.tdata={}
            self.tdata['valid_detailed'] = int(mileage)
            self.tdata['valid_approx'] = int(mileage)
            self.tdata['valid_unmapped'] = int(mileage)
            self.tdata['valid_total'] = int(mileage)
            self.tdata['all_detailed'] = int(mileage)
            self.tdata['all_approx'] = int(mileage)
            self.tdata['all_unmapped'] = int(mileage)
            self.tdata['all_total'] = int(mileage)

            return self.tdata


    def t1_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total):
        return self._t_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total)

    def t2_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total):
        return self._t_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total)

    def t3_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total):
        return self._t_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total)

    def t4_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total):
        return self._t_data(self, valid_detailed, valid_approx, valid_unmapped, valid_total, all_detailed, all_approx, all_unmapped, all_total)
    
    def miles_setter(region_num, row_val, col_val):
    roman_region = romNum_Reg[region_num]
    region_tab = "R{}_Prelim".format(roman_region)
    sheet = final_wb.sheet_by_name(region_tab)
    for row in range(80):
        for col in range(sheet.ncols):
            return sheet.cell_value(row_val, col_val)
    
    miles_map = {}
def miles_dict(region, name):
    miles_map[name] = miles_class(name)
    miles_map[name].t1_data['valid_detailed'] = miles_setter(region, region_map[region].t1_data['valid_all_row'], region_map[region].detailed_col)
    miles_map[name].t1_data['valid_approx'] = miles_setter(region, region_map[region].t1_data['valid_all_row'], region_map[region].approx_col)
    miles_map[name].t1_data['valid_unmapped'] = miles_setter(region, region_map[region].t1_data['valid_all_row'], region_map[region].unmapped_col)
    miles_map[name].t1_data['valid_total'] = miles_setter(region, region_map[region].t1_data['valid_all_row'], region_map[region].total_col)


