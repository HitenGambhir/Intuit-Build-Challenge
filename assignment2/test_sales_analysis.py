import unittest
import tempfile
from pathlib import Path

from sales_analysis import (
    read_sales,
    total_revenue,
    total_profit,
    revenue_by_region,
    profit_by_region,
    revenue_by_item_type,
    orders_by_channel,
    top_region_by_profit,
    average_units_per_order,
    revenue_by_month,
)


# Small sample dataset taken from your real CSV (same columns)
SAMPLE_CSV = """Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
Australia and Oceania,Tuvalu,Baby Food,Offline,H,5/28/2010,669165933,6/27/2010,9925,255.28,159.42,2533654.00,1582243.50,951410.50
Central America and the Caribbean,Grenada,Cereal,Online,C,8/22/2012,963881480,9/15/2012,2804,205.70,117.11,576782.80,328376.44,248406.36
Europe,Russia,Office Supplies,Offline,L,5/2/2014,341417157,5/8/2014,1779,651.21,524.96,1158502.59,933903.84,224598.75
Sub-Saharan Africa,Sao Tome and Principe,Fruits,Online,C,6/20/2014,514321792,7/5/2014,8102,9.33,6.92,75591.66,56065.84,19525.82
"""


class TestSalesAnalysis(unittest.TestCase):

    def _write_temp_csv(self) -> str:
        """Writes the sample CSV to a temp file so tests run independently."""
        tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, newline="", encoding="utf-8")
        tmp.write(SAMPLE_CSV)
        tmp.flush()
        tmp.close()
        return tmp.name

    # -----------------------------------------------------
    # BASIC LOAD TEST
    # -----------------------------------------------------
    def test_read_sales(self):
        path = self._write_temp_csv()
        records = read_sales(path)

        self.assertEqual(len(records), 4)
        self.assertEqual(records[0].region, "Australia and Oceania")
        self.assertEqual(records[1].item_type, "Cereal")

        Path(path).unlink(missing_ok=True)

    # -----------------------------------------------------
    # TOTAL REVENUE & PROFIT
    # -----------------------------------------------------
    def test_total_revenue_and_profit(self):
        path = self._write_temp_csv()
        records = read_sales(path)

        expected_revenue = (
            2533654.00 +
            576782.80 +
            1158502.59 +
            75591.66
        )

        expected_profit = (
            951410.50 +
            248406.36 +
            224598.75 +
            19525.82
        )

        self.assertAlmostEqual(total_revenue(records), expected_revenue)
        self.assertAlmostEqual(total_profit(records), expected_profit)

        Path(path).unlink(missing_ok=True)

    # -----------------------------------------------------
    # GROUPING TESTS
    # -----------------------------------------------------
    def test_region_item_channel_grouping(self):
        path = self._write_temp_csv()
        records = read_sales(path)

        # region revenue test
        by_region = revenue_by_region(records)
        self.assertAlmostEqual(by_region["Australia and Oceania"], 2533654.00)
        self.assertAlmostEqual(by_region["Europe"], 1158502.59)

        # item type revenue
        by_item = revenue_by_item_type(records)
        self.assertAlmostEqual(by_item["Baby Food"], 2533654.00)
        self.assertAlmostEqual(by_item["Cereal"], 576782.80)

        # channel grouping
        by_channel = orders_by_channel(records)
        self.assertEqual(by_channel["Offline"], 2)
        self.assertEqual(by_channel["Online"], 2)

        Path(path).unlink(missing_ok=True)

    # -----------------------------------------------------
    # PROFIT + TOP REGION
    # -----------------------------------------------------
    def test_top_region_by_profit(self):
        path = self._write_temp_csv()
        records = read_sales(path)

        by_prof = profit_by_region(records)
        self.assertAlmostEqual(by_prof["Australia and Oceania"], 951410.50)

        top = top_region_by_profit(records)
        self.assertEqual(top, "Australia and Oceania")

        Path(path).unlink(missing_ok=True)

    # -----------------------------------------------------
    # MONTHLY REVENUE + AVERAGE
    # -----------------------------------------------------
    def test_monthly_revenue_and_average_units(self):
        path = self._write_temp_csv()
        records = read_sales(path)

        by_month = revenue_by_month(records)
        self.assertAlmostEqual(by_month["2010-05"], 2533654.00)
        self.assertAlmostEqual(by_month["2012-08"], 576782.80)
        self.assertAlmostEqual(by_month["2014-05"], 1158502.59)
        self.assertAlmostEqual(by_month["2014-06"], 75591.66)

        total_units = 9925 + 2804 + 1779 + 8102
        self.assertAlmostEqual(average_units_per_order(records), total_units / 4)

        Path(path).unlink(missing_ok=True)

    # -----------------------------------------------------
    # VERBOSE DEMO OUTPUT (like assignment 1)
    # -----------------------------------------------------
    def test_verbose_output(self):
        print("\n=== SALES ANALYSIS VERBOSE DEMO (TEST OUTPUT) ===\n")

        path = self._write_temp_csv()
        records = read_sales(path)

        print("Loaded:", len(records), "records")
        print("Total Revenue:", total_revenue(records))
        print("Total Profit:", total_profit(records))
        print("Top Region:", top_region_by_profit(records))

        print("\nRevenue by Region:")
        for r, v in revenue_by_region(records).items():
            print(f"  {r}: {v}")

        print("\nRevenue by Month:")
        for m, v in revenue_by_month(records).items():
            print(f"  {m}: {v}")

        print("\n=== END OF VERBOSE DEMO ===\n")

        Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
