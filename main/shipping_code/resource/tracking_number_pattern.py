class TrackingNumberPattern:

    tracking_number_patterns ={
            '우체국': r'^\d{13}$|^\d{6}[-_]\d{7}$',
            '로젠택배': r'^\d{11}$|^\d{3}[-_]\d{4}[-_]\d{4}$',
            '일양로지스': r'^\d{9,11}$',
            'FedEx': r'^\d{12}$',
            '한진택배': r'^\d{10}$|^\d{12}$',
            '경동택배': r'^\d{9,16}$|^\d{4}-\d{3}-\d{6}$',
            '합동택배': r'^\d{9,16}$',
            '롯데택배': r'^\d{12}$|^\d{4}-\d{4}-\d{4}$',
            '농협택배': r'^\d{12}$',
            '호남택배': r'^\d{10}$',
            '천일택배': r'^\d{11}$',
            '대신택배': r'^\d{13}$',
            '건영택배': r'^\d{10}$',
            'CU편의점택배': r'^\d{10}$|^\d{12}$|^\d{4}[-_]\d{4}[-_]\d{4}$',
            'CVSnet편의점택배': r'^\d{10}$|^\d{12}$|^\d{4}[-_]\d{4}[-_]\d{4}$',
            '한덱스': r'^\d{10}$|^\d{14}$',
            'TNT Express': r'^\d{8,9}$',
            'USPS': r'^\d{10}$|^\d{22}$|^[A-Z]{2}\d{9}[A-Z]{2}$',
            'EMS': r'^[A-Z]{2}\d{9}[A-Z]{2}$',
            'DHL': r'^\d{10}$'
        }
