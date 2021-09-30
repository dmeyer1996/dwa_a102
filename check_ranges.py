# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:12:05 2021

@author: Edwin Echeverri Salazar & Daniel Meyer
"""

param_rages = {
    'P': [500, 1700, 'Precipitation', 'mm/a'], 
    'ETp' :[450, 700, 'Evapotranspiration', 'mm/a'], 
    'Sp_roof': [0.1, 0.6, 'Storage height (sp)', 'mm/a'],
    'Sp_flat_area': [0.6, 3, 'Storage height (sp)', 'mm'],
    'h_green_roof': [40, 500, 'Installation height (h)', 'mm'],
    'kf_green_roof': [18, 100, 'Hydraulic conductivity (kf)', 'mm/h'],
    'WKmax_WP_green_roof': [0.35, 0.65, 'Difference (wkmax_wp)', ''],
    'Sp_storage_roof': [3, 10, 'Storage height (sp)', 'mm'],
    'FA_permeable_surface': [2, 10, 'Joint ratio (fa)'],
    'Sp_permeable_surface': [0.1, 2, 'Storage height (sp)', 'mm'],
    'WKmax_WP_permeable_surface': [0.1, 0.2, 'Difference (wkmax_wp)'],
    'kf_permeable_surface': [6, 100, 'Hydraulic conductivity (kf)', 'mm/h'],
    'Sp_porous_surface': [2.5, 4.2, 'Storage height (sp)', 'mm'],
    'h_porous_surface': [50, 100, 'Installation height (h)', 'mm'],
    'kf_porous_surface': [10, 180, 'Hydraulic conductivity (kf)', 'mm/h'],
    'FA_paver_stonegrid': [20, 30, 'Joint ratio (fa)'],
    'Sp_paver_stonegrid': [0.1, 2, 'Storage height (sp)', 'mm'],
    'WKmax_WP_paver_stonegrid': [0.1, 0.2, 'Difference (wkmax_wp)'],
    'h_gravel_cover': [50, 100, 'Installation height (h)', 'mm'],
    'Sp_gravel_cover': [2.5, 4.2, 'Storage height (sp)', 'mm'],
    'kf_gravel_cover': [0.72, 10, 'Hydraulic conductivity (kf)', 'mm/h'],
    'kf_surf_infiltration': [325, 1100, 'Hydraulic conductivity (kf)', 'mm/h'],
    'kf_infilt_swale': [14, 3600, 'Hydraulic conductivity (kf)', 'mm/h'],
    'kf_swale_trench': [3.6, 36, 'Hydraulic conductivity (kf)', 'mm/h'],
    'qDr_swale_trench_system': [1, 10, 'Throttled discharge yield (qdr)'],
    'kf_swale_trench_system': [0.36, 3.6, 'Hydraulic conductivity (kf)', 'mm/h'],
    'VSp_rainwater_usage': [10, 200, 'Specific storage volume (vsp)', 'mm'],
    'VBr_rainwater_usage': [0, 5, 'Available water volume (vbr)', 'mm/d'],
    'FAbw_rainwater_usage': [0, 5, 'Proportion of irrigated area (fabw)', ''],
    'qBw_rainwater_usage': [0, 200, 'Specific annual requirement for irrigation (qbw)', 'l/(m^2*year)'],
    'a_1_pod_system': [0.0, 1.0, 'Proportion of area 1 (a_1)', ''],
    'a_2_pod_system': [0.0, 1.0, 'Proportion of area 2 (a_2)', ''],
    'a_3_pod_system': [0.0, 1.0, 'Proportion of area 3 (a_3)', ''],
    'a_4_pod_system': [0.0, 1.0, 'Proportion of area 4 (a_4)', ''],
    }

'''
Surface specific particle runoff for AFS 63 by category in kg/(ha*a)
National Average of h=800 mm/a and effective h_eff=560 mm/a
'''
b_1=280 #kg/(ha*a)
b_2=530 #kg/(ha*a)
b_3=760 #kg/(ha*a)

surface_use = {
    'D': [1, b_1, 'Dachflaechen(D) ; Roof surface(D)'],
    'VW1': [1,b_1, 'Hof- und Wegeflaechen(VW)  ; yard and path areas(VW)'],
    'V1': [1, b_1, 'Verkehrsflaechen(V1) ; traffic areas (V1)'],
    'VW2': [2, b_2, 'Hof- und Wegeflaechen(VW2)  ; yard and path areas(VW2)'],
    'V2': [2, b_2, 'Verkehrsflaechen(V2) ; traffic areas (V2)'],
    'V3': [3, b_3, 'Verkehrsflaechen(V3) ; traffic areas (V3)'],
    'BG1': [1, b_1, 'Gleisanlage(G); (railway) track system(G)'],
    'BF': [2, b_2, 'Start- und Landebahnen und weitere Betriebsflaechen von Flughaefen(F) ;'
              'Runways and other operational areas of airports(F)'],
    'BL': [2, b_2, 'landwirtschaftliche Hofflaechen(L) ; agricultural yard areas(L)'],
    'BG2': [2, b_2, 'Gleisanlage(G2); (railway) track system(G2)'],
    'SD1': [2, b_2, 'Dachflaechen(D1) ; Roof surface(D1)'],
    'SD2': [3, b_3, 'Dachflaechen(D2) ; Roof surface(D2)'],
    'SV': [3, b_3, 'Hof- und Verkehrsflaechen sowie Park- und Stellplaetze(V) ;'
              'Yard and traffic areas as well as parking spaces(V)'],
    'SF': [3, b_3, 'Flaechen von Flughaefen mit besonderer Belastung(SF) ; '
              'areas of airports with special substance contamination(SF)'],
    'SL': [3, b_3, 'landwirtschaftliche Hofflaechen und sonstige Flaechen(L) ;'
              'agricultural yard areas and other areas(L)'],
    'BG3': [3, b_3, 'Gleisanlage(G3); (railway) track system (G3)'],
    'SG': [3, b_3, 'Gleisanlage mit besonderer Belastung(SG); '
               '(railway) track system with special substance contamination (SG)'],
    'SA': [3, b_3, 'Hof- und Verkehrsflaechen auf Abwasser- und Abfallanlagen(A) ;'
              'Yard and traffic areas on sewage and waste facilities(A)']
    }



def validRange(val, param):
    ''' generic function to check parameter range'''
    
    if ( (val < param_rages[param][0]) or (val > param_rages[param][1]) ): 
        raise Exception(f"{param_rages[param][2]} is not valid."
                        f" Acceptable range: {param_rages[param][0]} - {param_rages[param][1]}"
                        f" {param_rages[param][3]}")


def validUse(param):
    ''' generic function to check correct surface use'''
    if not surface_use[param]:
        raise Exception(f"{[param]} is not valid.")

def get_b(param):
    ''' generic function to get b for given correct Surface'''
    if surface_use[param]:
        b=surface_use[param][1]
        return b

def get_category(param):
    ''' generic function to get Surface Category for given correct Surface'''
    if surface_use[param]:
        surface_category = surface_use[param][0]
        return surface_category